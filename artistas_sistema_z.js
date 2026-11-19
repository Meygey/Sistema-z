/**
 * SISTEMA Z - MÓDULO DE ARTISTAS Y PERFILES
 */

const Z_DEBUG = true;

function zLog(modulo, mensaje, tipo = "INFO") {
    if (!Z_DEBUG) return;
    console.log(`[Z-CORE][${modulo}][${tipo}] ${mensaje}`);
}

window.SistemaZArtistas = {
    init() {
        zLog("ARTISTAS", "Módulo de artistas inicializado.");
        if (typeof window.cargarCatalogoSupabase === "function") {
            window.cargarCatalogoSupabase();
        }
    }
};
