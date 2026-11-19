/**
 * 🔺 SISTEMA Z - INTERFAZ DE REGISTRO Y PERFILES DE ARTISTAS
 */
(function() {
    console.log("[Z-UI] Inicializando interfaz de artistas...");

    function actualizarEstadoUI() {
        const userEl = document.getElementById('z-current-user');
        const btnAuth = document.getElementById('z-btn-auth');
        const artista = window.SistemaZArtistas ? window.SistemaZArtistas.obtenerArtistaActivo() : "";

        if (userEl) {
            if (artista) {
                userEl.textContent = "Artista: " + artista;
                userEl.style.color = "#ff4d4d";
                userEl.style.fontWeight = "bold";
            } else {
                userEl.textContent = "Modo Público";
                userEl.style.color = "#888";
                userEl.style.fontWeight = "normal";
            }
        }
        if (btnAuth) {
            btnAuth.textContent = artista ? "Perfil / Salir" : "Acceder";
        }
    }

    function abrirModalArtista() {
        if (document.getElementById('z-auth-modal')) return;
        const actual = window.SistemaZArtistas ? window.SistemaZArtistas.obtenerArtistaActivo() : "";

        const modal = document.createElement('div');
        modal.id = 'z-auth-modal';
        modal.style.cssText = `
            position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 100000;
            display: flex; align-items: center; justify-content: center; padding: 16px;
            font-family: monospace; color: #fff;
        `;

        modal.innerHTML = `
            <div style="background: #111; border: 2px solid #ff1a1a; border-radius: 8px; max-width: 380px; width: 100%; padding: 18px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <strong style="color:#ff1a1a; font-size:15px;">🔺 PERFIL DE ARTISTA Z</strong>
                    <button id="z-modal-close" style="background:none; border:none; color:#aaa; font-size:18px; cursor:pointer;">✕</button>
                </div>
                <p style="font-size:12px; color:#ccc; margin-bottom:12px;">
                    Inicia con tu nombre artístico exacto para habilitar el borrado solo en tus temas.
                </p>
                <label style="display:block; font-size:11px; color:#aaa; margin-bottom:4px;">Nombre del Artista</label>
                <input id="z-auth-name" type="text" value="${actual.replace(/"/g, '&quot;')}" placeholder="Ej: Enyi el Científico"
                    style="width:100%; padding:8px; margin-bottom:10px; background:#000; color:#fff; border:1px solid #444; border-radius:4px; font-size:13px;" />
                <label style="display:block; font-size:11px; color:#aaa; margin-bottom:4px;">PIN / Clave local (opcional)</label>
                <input id="z-auth-pin" type="password" placeholder="Solo en este dispositivo"
                    style="width:100%; padding:8px; margin-bottom:14px; background:#000; color:#fff; border:1px solid #444; border-radius:4px; font-size:13px;" />
                <div style="display:flex; gap:8px; justify-content:flex-end;">
                    ${actual ? `<button id="z-auth-logout" style="background:#27272a; color:#fff; border:1px solid #555; padding:7px 12px; border-radius:4px; cursor:pointer; font-size:12px;">Cerrar sesión</button>` : ""}
                    <button id="z-auth-save" style="background:#ff1a1a; color:#fff; border:none; padding:7px 14px; border-radius:4px; cursor:pointer; font-weight:bold; font-size:12px;">Entrar</button>
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        document.getElementById('z-modal-close').addEventListener('click', () => modal.remove());
        document.getElementById('z-auth-save').addEventListener('click', () => {
            const nombre = document.getElementById('z-auth-name').value;
            const pin = document.getElementById('z-auth-pin').value;
            const res = window.SistemaZArtistas.iniciarSesionArtista(nombre, pin);
            if (!res.ok) {
                alert("⚠️ " + res.msg);
                return;
            }
            actualizarEstadoUI();
            modal.remove();
        });

        const logoutBtn = document.getElementById('z-auth-logout');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => {
                window.SistemaZArtistas.cerrarSesionArtista();
                actualizarEstadoUI();
                modal.remove();
            });
        }
    }

    function crearBarraArtistas() {
        if (document.getElementById('z-artist-bar')) return;

        const bar = document.createElement('div');
        bar.id = 'z-artist-bar';
        bar.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; background: #0a0a0a;
            border-bottom: 2px solid #ff1a1a; color: #fff; padding: 8px 15px;
            display: flex; justify-content: space-between; align-items: center;
            z-index: 99999; font-family: monospace; font-size: 14px;
        `;

        bar.innerHTML = `
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="color: #ff1a1a; font-weight: bold;">🔺 SISTEMA Z</span>
                <span id="z-current-user" style="color: #888;">Modo Público</span>
            </div>
            <div>
                <button onclick="window.EstudioReelsZ && window.EstudioReelsZ.abrirEstudio()" style="background: #1a1a1a; color: #ff1a1a; border: 1px solid #ff1a1a; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-weight: bold; margin-right: 6px;">🎥 Reel</button>
                <button id="z-btn-auth" style="background: #ff1a1a; color: #fff; border: none; padding: 5px 12px; border-radius: 4px; cursor: pointer; font-weight: bold;">Acceder</button>
            </div>
        `;

        document.body.prepend(bar);
        document.body.style.marginTop = "45px";

        document.getElementById('z-btn-auth').addEventListener('click', abrirModalArtista);
        window.addEventListener('sistemaZ:artistaCambio', actualizarEstadoUI);
        actualizarEstadoUI();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', crearBarraArtistas);
    } else {
        crearBarraArtistas();
    }
})();
