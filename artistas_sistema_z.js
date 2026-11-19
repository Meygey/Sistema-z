/**
 * 🔺 SISTEMA Z - MÓDULO DE ARTISTAS Y PERFILES
 */
const Z_DEBUG = true;
const STORAGE_ARTISTA_KEY = "sistema_z_artista_activo";
const STORAGE_PIN_KEY = "sistema_z_artista_pin";

function zLog(modulo, mensaje, tipo = "INFO") {
    if (!Z_DEBUG) return;
    console.log(`[Z-CORE][${modulo}][${tipo}] ${mensaje}`);
}

function normalizarNombreArtista(nombre) {
    return (nombre || "").trim().replace(/\s+/g, " ").toLowerCase();
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

    iniciarSesionArtista(nombreArtista, pin = "") {
        const limpio = (nombreArtista || "").trim().replace(/\s+/g, " ");
        if (!limpio) {
            return { ok: false, msg: "Ingresa tu nombre artístico." };
        }
        try {
            const pinGuardado = localStorage.getItem(STORAGE_PIN_KEY + ":" + normalizarNombreArtista(limpio));
            if (pinGuardado && pinGuardado !== pin) {
                return { ok: false, msg: "Clave/PIN incorrecto para este perfil de artista." };
            }
            if (!pinGuardado && pin) {
                localStorage.setItem(STORAGE_PIN_KEY + ":" + normalizarNombreArtista(limpio), pin);
            }
            localStorage.setItem(STORAGE_ARTISTA_KEY, limpio);
            const artistInput = document.getElementById("artistName");
            if (artistInput && !artistInput.value.trim()) {
                artistInput.value = limpio;
            }
            window.dispatchEvent(new CustomEvent("sistemaZ:artistaCambio", { detail: { artista: limpio } }));
            if (typeof window.cargarCatalogoSupabase === "function") {
                window.cargarCatalogoSupabase();
            }
            zLog("ARTISTAS", `Sesión iniciada como: ${limpio}`);
            return { ok: true, artista: limpio };
        } catch (err) {
            return { ok: false, msg: err.message };
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
            const url = `${SUPABASE_URL}/rest/v1/temas_z?id=eq.${encodeURIComponent(id)}`;
            const res = await fetch(url, {
                method: "DELETE",
                headers: {
                    "apikey": SUPABASE_ANON_KEY,
                    "Authorization": `Bearer ${SUPABASE_ANON_KEY}`,
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
