with open('index.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Z | Tierra de Mafia</title>
    <style>
        body {
            background-color: #030303;
            color: #f0f0f0;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 15px;
            text-align: center;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        header {
            border-bottom: 2px solid #ff0000;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        h1 {
            color: #ff0000;
            font-size: 24px;
            margin: 5px 0;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .subtitle {
            color: #888;
            font-size: 12px;
        }
        .card {
            background: #0a0a0a;
            border: 1px solid #ff0000;
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            text-align: left;
            box-shadow: 0 4px 20px rgba(255, 0, 0, 0.2);
        }
        .card h3 {
            color: #ff2222;
            margin-top: 0;
            font-size: 16px;
        }
        input[type="text"], input[type="file"], select {
            background: #111;
            border: 1px solid #444;
            color: #fff;
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
            border-radius: 6px;
            margin-bottom: 10px;
            font-size: 13px;
        }
        button {
            background: #ff0000;
            color: #fff;
            border: none;
            padding: 12px;
            border-radius: 6px;
            font-weight: bold;
            width: 100%;
            cursor: pointer;
            font-size: 14px;
            text-transform: uppercase;
            margin-top: 5px;
        }
        button:hover {
            background: #cc0000;
        }
        audio, video {
            width: 100%;
            margin-top: 8px;
            border-radius: 6px;
        }
        .btn-action {
            display: inline-block;
            text-align: center;
            background: #1a1a1a;
            border: 1px solid #ff0000;
            color: #ff2222;
            padding: 8px 12px;
            margin-top: 6px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
            box-sizing: border-box;
        }
        .row-btns {
            display: flex;
            gap: 8px;
            margin-top: 8px;
        }
        /* Estética Reel / Test 416Hz */
        #reel-viewport {
            position: relative;
            width: 100%;
            height: 320px;
            background: #000;
            border: 2px solid #ff0000;
            border-radius: 8px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        #reel-video-preview {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: none;
        }
        .reel-overlay-text {
            position: absolute;
            background: rgba(0, 0, 0, 0.75);
            color: #fff;
            padding: 6px 12px;
            border-left: 3px solid #ff0000;
            font-size: 13px;
            font-weight: bold;
            z-index: 5;
            text-align: left;
        }
        #text-top { top: 15px; left: 15px; right: 15px; }
        #text-bottom { bottom: 15px; left: 15px; right: 15px; text-align: center; color: #ff3333; }
        
        #flash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: red;
            opacity: 0;
            pointer-events: none;
            z-index: 9999;
            transition: opacity 0.08s ease;
        }
    </style>
</head>
<body>
    <div id="flash-screen"></div>
    <div class="container">
        <header>
            <h1>Sistema Z 🔺 416Hz</h1>
            <div class="subtitle">Tierra de Mafia • Enyi el Científico</div>
        </header>

        <!-- BUSCADOR GLOBAL -->
        <div class="card">
            <h3>🔍 Buscador Global Z</h3>
            <input type="text" id="global-search-input" placeholder="🔎 Busca temas o reels...">
            <div id="search-status" style="font-size:11px; color:#00ffcc; margin-top:4px;">Catálogo activo.</div>
        </div>

        <!-- ESTUDIO Z: CREADOR DE REELS / TEST 416HZ -->
        <div class="card" style="border: 2px solid #ff0000; background: #0f0000;">
            <h3>🎛️ Estudio Z: Creador de Reels & Test 416Hz</h3>
            <p style="font-size: 12px; color: #aaa;">Monta tu video vertical, activa el pulso flash y genera tu contenido para la calle.</p>
            
            <!-- Vista previa del Reel con textos superpuestos -->
            <div id="reel-viewport">
                <div id="text-top" class="reel-overlay-text">¿Tu cel vibra con el 416Hz? 🧪</div>
                <video id="reel-video-preview" controls playsinline></video>
                <div id="placeholder-cam" style="color: #666; font-size: 13px; padding: 20px;">
                    🎥 Sube o graba tu video para activar el Reel Z
                </div>
                <div id="text-bottom" class="reel-overlay-text">Súbelo a tope y pon la mano encima. 👺</div>
            </div>

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Título del Reel / Tema:</label>
            <input type="text" id="upload-title" placeholder="Ej. Bandido - POV #1">

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Seleccionar Video (MP4 de la Galería):</label>
            <input type="file" id="upload-media" accept="video/*" onchange="previewReelVideo(this)">

            <div class="row-btns">
                <button type="button" onclick="toggleFlashBeat()" id="flash-btn" style="background:#220000; border:1px solid #ff0000; color:#ff4444; flex:1;">⚡ Pulso Flash</button>
                <button type="button" id="publish-btn" style="flex:2;">🚀 Publicar Reel en el Muro</button>
            </div>
        </div>

        <!-- MURO / FEED DE REELS Y TEMAS -->
        <div id="pro-feed"></div>
    </div>

    <script>
        let flashInterval = null;

        document.addEventListener('DOMContentLoaded', () => {
            loadFeed();
            document.getElementById('publish-btn').addEventListener('click', handlePublish);
            
            const searchInput = document.getElementById('global-search-input');
            if(searchInput) {
                searchInput.addEventListener('input', executeGlobalSearch);
            }
        });

        function previewReelVideo(input) {
            if (input.files && input.files[0]) {
                const file = input.files[0];
                const url = URL.createObjectURL(file);
                const videoEl = document.getElementById('reel-video-preview');
                const placeholder = document.getElementById('placeholder-cam');
                
                videoEl.src = url;
                videoEl.style.display = 'block';
                placeholder.style.display = 'none';
            }
        }

        function handlePublish(e) {
            e.preventDefault();
            const title = document.getElementById('upload-title').value.trim() || 'Bandido - POV #1';
            const mediaInput = document.getElementById('upload-media');

            if (!mediaInput.files || mediaInput.files.length === 0) {
                alert('⚠️ Selecciona un video MP4 para armar tu Reel en el Estudio Z.');
                return;
            }

            const mediaFile = mediaInput.files[0];
            const reader = new FileReader();
            reader.onload = function(ev) {
                const mediaUrl = ev.target.result;
                saveReelData(title, mediaUrl);
            };
            reader.readAsDataURL(mediaFile);
        }

        function saveReelData(title, mediaUrl) {
            const embedCode = `<iframe src="https://meygey.github.io/Sistema-z/" width="100%" height="280" style="background:#000;border:1px solid #ff0000;border-radius:8px;" title="${title}"></iframe>`;
            const track = { id: 'reel_' + Date.now(), title, mediaUrl, embedCode };

            let saved = JSON.parse(localStorage.getItem('sistema_z_reels') || '[]');
            saved.unshift(track);
            localStorage.setItem('sistema_z_reels', JSON.stringify(saved));

            loadFeed();
            document.getElementById('upload-title').value = '';
            document.getElementById('upload-media').value = '';
            document.getElementById('reel-video-preview').style.display = 'none';
            document.getElementById('placeholder-cam').style.display = 'block';
            alert('✅ ¡Reel publicado en el Muro del Sistema Z!');
        }

        function loadFeed() {
            let saved = JSON.parse(localStorage.getItem('sistema_z_reels') || '[]');
            const feed = document.getElementById('pro-feed');
            feed.innerHTML = '';
            
            if (saved.length === 0) {
                feed.innerHTML = '<div class="card" style="text-align:center; color:#888; font-size:13px;">No hay reels publicados aún. Usa el <strong>Estudio Z</strong> arriba para armar y subir tus videos de la calle.</div>';
                return;
            }

            saved.forEach(track => renderCard(track));
        }

        function renderCard(track) {
            const card = document.createElement('div');
            card.className = 'card track-post-card';
            card.innerHTML = `
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span style="color:#ff2222; font-weight:bold; font-size:15px;">🔥 ${track.title}</span>
                    <span style="background:#220000; color:#ff4444; padding:2px 6px; border-radius:4px; font-size:10px;">REEL Z 416Hz</span>
                </div>
                <div style="position:relative; width:100%; background:#000; border-radius:6px; overflow:hidden;">
                    <div style="position:absolute; top:10px; left:10px; right:10px; background:rgba(0,0,0,0.75); color:#fff; padding:4px 8px; border-left:3px solid #ff0000; font-size:11px; font-weight:bold; z-index:5;">¿Tu cel vibra con el 416Hz? 🧪</div>
                    <video controls src="${track.mediaUrl}" style="width:100%; max-height:280px; object-fit:cover; display:block;"></video>
                    <div style="position:absolute; bottom:10px; left:10px; right:10px; background:rgba(0,0,0,0.75); color:#ff3333; padding:4px 8px; font-size:11px; font-weight:bold; z-index:5; text-align:center;">Súbelo a tope y pon la mano encima. 👺</div>
                </div>
                <div class="row-btns" style="margin-top:10px;">
                    <button onclick="navigator.clipboard.writeText('${window.location.href}'); alert('🔗 ¡Enlace del Reel copiado!');" class="btn-action" style="flex:1; background:#1a1a1a; color:#fff; border:1px solid #444;">🔗 Compartir</button>
                    <button onclick="deleteReel('${track.id}')" class="btn-action" style="background:#300; color:#ff6666; border:1px solid #ff0000;">🗑️ Borrar</button>
                </div>
                <div style="margin-top:8px;">
                    <span style="font-size:10px; color:#888;">Formato de Código (Embed):</span>
                    <textarea style="background:#000; color:#00ffcc; border:1px solid #333; width:100%; height:45px; font-family:monospace; font-size:10px; padding:4px; border-radius:4px; box-sizing:border-box; resize:none;" readonly>${track.embedCode}</textarea>
                </div>
            `;
            feed.appendChild(card);
        }

        function deleteReel(id) {
            if (confirm('¿Eliminar este Reel del sistema?')) {
                let saved = JSON.parse(localStorage.getItem('sistema_z_reels') || '[]');
                saved = saved.filter(t => t.id !== id);
                localStorage.setItem('sistema_z_reels', JSON.stringify(saved));
                loadFeed();
            }
        }

        function toggleFlashBeat() {
            const screen = document.getElementById('flash-screen');
            const btn = document.getElementById('flash-btn');
            if (flashInterval) {
                clearInterval(flashInterval);
                flashInterval = null;
                screen.style.opacity = '0';
                btn.innerText = '⚡ Pulso Flash';
                btn.style.background = '#220000';
            } else {
                btn.innerText = '🛑 Detener Flash';
                btn.style.background = '#ff0000';
                btn.style.color = '#fff';
                let state = false;
                flashInterval = setInterval(() => {
                    state = !state;
                    screen.style.opacity = state ? '0.25' : '0';
                }, 310);
            }
        }

        function executeGlobalSearch() {
            const query = document.getElementById('global-search-input').value.toLowerCase().trim();
            const cards = document.querySelectorAll('.track-post-card');
            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                card.style.display = (query === '' || text.includes(query)) ? 'block' : 'none';
            });
        }
    </script>
</body>
</html>
""")

print('¡ESTUDIO Z RESTAURADO: CREADOR DE REELS Y TEST 416HZ ACTIVOS!')
