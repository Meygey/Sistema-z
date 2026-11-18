/**
 * 🔺 SISTEMA Z - INTERFAZ DE REGISTRO Y PERFILES DE ARTISTAS
 * Módulo visual independiente para la gestión de cuentas en Supabase.
 */

(function() {
    console.log("[Z-UI] Inicializando interfaz de artistas...");

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
                <button id="z-btn-auth" style="background: #ff1a1a; color: #fff; border: none; padding: 5px 12px; border-radius: 4px; cursor: pointer; font-weight: bold;">Acceder / Registrar</button>
            </div>
        `;

        document.body.prepend(bar);

        // Ajustar el margen superior del body para que la barra no tape el contenido
        document.body.style.marginTop = "45px";

        document.getElementById('z-btn-auth').addEventListener('click', () => {
            alert("🔺 Consola de Autenticación Z: Módulo de perfiles activo. Próximo paso: Vínculo con Supabase.");
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', crearBarraArtistas);
    } else {
        crearBarraArtistas();
    }
})();
