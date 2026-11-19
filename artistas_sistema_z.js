/**
 * 🔺 SISTEMA Z - MÓDULO DE ARTISTAS Y PERFILES (SEGURIDAD MULTI-DISPOSITIVO)
 */
const Z_DEBUG = true;
const STORAGE_ARTISTA_KEY = "sistema_z_artista_activo";
const STORAGE_PIN_HASH_KEY = "sistema_z_artista_pin_hash";

function zLog(modulo, mensaje, tipo = "INFO") {
    if (!Z_DEBUG) return;
    console.log(`[Z-CORE][${modulo}][${tipo}] ${mensaje}`);
}

function normalizarNombreArtista(nombre) {
    return (nombre || "").trim().replace(/\s+/g, " ").toLowerCase();
}

async function sha256Hex(texto) {
    const data = new TextEncoder().encode(texto);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    return Array.from(new Uint8Array(hashBuffer))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
}

function getSupabaseConfig() {
    return {
        url: typeof SUPABASE_URL !== "undefined" ? SUPABASE_URL : "https://uxyvpqraebwptbbvngus.supabase.co",
        key: typeof SUPABASE_ANON_KEY !== "undefined" ? SUPABASE_ANON_KEY : ""
    };
}

async function consultarPerfilRemoto(artistaNorm) {
    const { url, key } = getSupabaseConfig();
    if (!key) return { status: "no_key", data: null };
    const endpoint = `${url}/rest/v1/perfiles_z?artista_key=eq.${encodeURIComponent(artistaNorm)}&select=*`;
    const res = await fetch(endpoint, {
        headers: {
            "apikey": key,
            "Authorization": `Bearer ${key}`
        }
    });
    if (res.status === 404 || res.status === 400) {
        return { status: "missing_table", data: null };
    }
    if (!res.ok) {
        const txt = await res.text();
        throw new Error(`Supabase perfiles_z (${res.status}): ${txt}`);
    }
    const rows = await res.json();
    return { status: "ok", data: Array.isArray(rows) && rows.length > 0 ? rows[0] : null };
}

async function crearPerfilRemoto(artistaNombre, artistaNorm, pinHash) {
    const { url, key } = getSupabaseConfig();
    if (!key) return false;
    const endpoint = `${url}/rest/v1/perfiles_z`;
    const res = await fetch(endpoint, {
        method: "POST",
        headers: {
            "apikey": key,
            "Authorization": `Bearer ${key}`,
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        },
        body: JSON.stringify({
            artista: artistaNombre,
            usuario: artistaNorm,
            artista_key: artistaNorm,
            artista_nombre: artistaNombre,
            pin_hash: pinHash
        })
    });
    return res.ok;
}

window.SistemaZArtistas = {
    init() {
        zLog("ARTISTAS", "Módulo de artistas inicializado.");
        if (typeof window.cargarCatalogoSupabase === "function") {
            window.cargarCatalogoSupabase();
        }
    },

    obtenerArtistaActivo() {
        try {
            return (localStorage.getItem(STORAGE_ARTISTA_KEY) || "").trim();
        } catch (_) {
            return "";
        }
    },

    esDuenoDelTema(nombreArtistaTema) {
        const activo = normalizarNombreArtista(this.obtenerArtistaActivo());
        const dueno = normalizarNombreArtista(nombreArtistaTema);
        return Boolean(activo && dueno && activo === dueno);
    },

    async iniciarSesionArtista(nombreArtista, pin = "") {
        const limpio = (nombreArtista || "").trim().replace(/\s+/g, " ");
        const clave = (pin || "").trim();
        if (!limpio) {
            return { ok: false, msg: "Ingresa tu nombre artístico." };
        }
        if (!clave || clave.length < 4) {
            return { ok: false, msg: "Ingresa una clave o PIN de al menos 4 caracteres para proteger tu perfil." };
        }

        const norm = normalizarNombreArtista(limpio);
        const pinHash = await sha256Hex(`${norm}::${clave}`);

        try {
            const remoto = await consultarPerfilRemoto(norm);

            if (remoto.status === "ok" && remoto.data) {
                if (remoto.data.pin_hash && remoto.data.pin_hash !== pinHash) {
                    return { ok: false, msg: "Clave incorrecta para este artista en el sistema." };
                }
            } else if (remoto.status === "ok" && !remoto.data) {
                const creado = await crearPerfilRemoto(limpio, norm, pinHash);
                if (!creado) {
                    return { ok: false, msg: "No se pudo registrar el perfil en Supabase. Revisa permisos de perfiles_z." };
                }
            } else if (remoto.status === "missing_table") {
                const localHash = localStorage.getItem(STORAGE_PIN_HASH_KEY + ":" + norm);
                if (localHash && localHash !== pinHash) {
                    return { ok: false, msg: "Clave incorrecta en este dispositivo." };
                }
                if (!localHash) {
                    localStorage.setItem(STORAGE_PIN_HASH_KEY + ":" + norm, pinHash);
                }
            }

            localStorage.setItem(STORAGE_ARTISTA_KEY, limpio);
            localStorage.setItem(STORAGE_PIN_HASH_KEY + ":" + norm, pinHash);

            const artistInput = document.getElementById("artistName");
            if (artistInput && !artistInput.value.trim()) {
                artistInput.value = limpio;
            }

            window.dispatchEvent(new CustomEvent("sistemaZ:artistaCambio", { detail: { artista: limpio } }));
            if (typeof window.cargarCatalogoSupabase === "function") {
                window.cargarCatalogoSupabase();
            }

            const aviso = remoto.status === "missing_table"
                ? " (Modo local: crea la tabla perfiles_z en Supabase para sincronizar entre dispositivos)"
                : " (Sincronizado en Supabase)";
            zLog("ARTISTAS", `Sesión iniciada como: ${limpio}${aviso}`);
            return { ok: true, artista: limpio, aviso };
        } catch (err) {
            return { ok: false, msg: "Error validando perfil: " + err.message };
        }
    },

    cerrarSesionArtista() {
        try {
            localStorage.removeItem(STORAGE_ARTISTA_KEY);
            window.dispatchEvent(new CustomEvent("sistemaZ:artistaCambio", { detail: { artista: "" } }));
            if (typeof window.cargarCatalogoSupabase === "function") {
                window.cargarCatalogoSupabase();
            }
            zLog("ARTISTAS", "Sesión de artista cerrada.");
        } catch (err) {
            zLog("ARTISTAS", "Error cerrando sesión: " + err.message, "ERROR");
        }
    },

    async eliminarTema(id, artistaTema) {
        if (!this.esDuenoDelTema(artistaTema)) {
            alert("⛔ Solo el artista dueño de este tema puede eliminarlo.");
            return;
        }
        const confirmar = confirm(`¿Seguro que deseas eliminar este tema de "${artistaTema}" del catálogo?`);
        if (!confirmar) return;

        try {
            const { url, key } = getSupabaseConfig();
            const endpoint = `${url}/rest/v1/temas_z?id=eq.${encodeURIComponent(id)}`;
            const res = await fetch(endpoint, {
                method: "DELETE",
                headers: {
                    "apikey": key,
                    "Authorization": `Bearer ${key}`,
                    "Prefer": "return=minimal"
                }
            });
            if (!res.ok) {
                const errTxt = await res.text();
                throw new Error(`HTTP ${res.status}: ${errTxt}`);
            }
            if (typeof debugLog === "function") {
                debugLog(`Tema eliminado de Supabase (ID: ${id}).`);
            }
            if (typeof window.cargarCatalogoSupabase === "function") {
                window.cargarCatalogoSupabase();
            }
        } catch (err) {
            if (typeof debugLog === "function") {
                debugLog("Error eliminando tema: " + err.message, true);
            }
            alert("🔴 No se pudo eliminar el tema: " + err.message);
        }
    }
};
