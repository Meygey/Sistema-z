/**
 * SISTEMA Z - MÓDULO DE ARTISTAS Y CATÁLOGO
 */

const Z_DEBUG = true;

function zLog(modulo, mensaje, tipo = "INFO") {
    if (!Z_DEBUG) return;
    console.log(`[Z-CORE][${modulo}][${tipo}] ${mensaje}`);
}

window.SistemaZArtistas = {
    init() {
        zLog("ARTISTAS", "Módulo inicializado.");
        this.cargarCatalogoSupabase();
    },

    async cargarCatalogoSupabase() {
        zLog("SUPABASE", "Conectando al catálogo temas_z...");
        try {
            const { data, error } = await window.supabaseClient.from('temas_z').select('*');
            if (error) throw error;
            
            zLog("SUPABASE", `Se cargaron ${data ? data.length : 0} temas con éxito.`);
            
            // Buscamos el contenedor original de tu diseño sin alterar clases ajenas
            const contenedor = document.getElementById('catalogo-contenedor') || document.querySelector('.catalogo-soberano');
            if (contenedor && data) {
                contenedor.innerHTML = data.map(t => `
                    <div class="tema-item" style="padding: 10px; border-bottom: 1px solid #333;">
                        <span style="color: #ff0033; font-weight: bold;">${t.artist || t.artista || 'Artista'}</span> - 
                        <span style="color: #fff;">${t.title || t.titulo || 'Tema'}</span>
                    </div>
                `).join('');
            }
        } catch (err) {
            zLog("SUPABASE", err.message, "ERROR");
        }
    }
};

document.addEventListener("DOMContentLoaded", () => {
    window.SistemaZArtistas.init();
});


