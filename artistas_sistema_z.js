/**
 * SISTEMA Z - MÓDULO DE ARTISTAS, PERFILES Y CATÁLOGO
 */

const Z_DEBUG = true;

function zLog(modulo, mensaje, tipo = "INFO") {
    if (!Z_DEBUG) return;
    const marca_tiempo = new Date().toLocaleTimeString();
    const prefijo = `[Z-CORE][${marca_tiempo}][${modulo}][${tipo}]`;
    console.log(`${prefijo} ${mensaje}`);
}

window.SistemaZArtistas = {
    init() {
        zLog("ARTISTAS", "Módulo inicializado con éxito.");
        this.cargarCatalogoSupabase();
    },

    async cargarCatalogoSupabase() {
        zLog("SUPABASE", "Conectando al catálogo temas_z...");
        try {
            const { data, error } = await window.supabaseClient.from('temas_z').select('*');
            if (error) throw error;
            
            zLog("SUPABASE", `Se cargaron ${data ? data.length : 0} temas con éxito.`);
            
            const contenedor = document.getElementById('catalogo-contenedor') || document.querySelector('.catalogo-soberano');
            if (contenedor && data) {
                contenedor.innerHTML = data.map(t => `<div class="tema-card"><strong>${t.artist}</strong> - ${t.title}</div>`).join('');
            }
        } catch (err) {
            zLog("SUPABASE", err.message, "ERROR");
        }
    }
};

document.addEventListener("DOMContentLoaded", () => {
    window.SistemaZArtistas.init();
});
