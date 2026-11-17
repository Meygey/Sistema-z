with open('index.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Z | Tierra de Mafia</title>
    <style>
        body {
            background-color: #050505;
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
            background: #0f0f0f;
            border: 1px solid #ff0000;
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            text-align: left;
            box-shadow: 0 4px 15px rgba(255, 0, 0, 0.15);
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
        textarea.code-box {
            background: #000;
            color: #00ffcc;
            border: 1px solid #333;
            width: 100%;
            height: 50px;
            font-family: monospace;
            font-size: 11px;
            padding: 6px;
            border-radius: 4px;
            box-sizing: border-box;
            margin-top: 5px;
            resize: none;
        }
        #flash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: red;
            opacity: 0;
            pointer-events: none;
            z-index: 9999;
            transition: opacity 0.1s ease;
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
            <input type="text" id="global-search-input" placeholder="🔎 Busca temas o artistas...">
            <div id="search-status" style="font-size:11px; color:#00ffcc; margin-top:4px;">Catálogo activo.</div>
        </div>

        <!-- ESTUDIO Z: TEST 416HZ -->
        <div class="card" style="border: 2px solid #ff2222; background: #120000;">
            <h3>👺 Estudio Z & Test 416Hz (Flash al Beat)</h3>
            <p style="font-size: 12px; color: #aaa;">Pulso lumínico subconsciente y frecuencia de la calle.</p>
            <button onclick="toggleFlashBeat()" id="flash-btn" style="background:#220000; border:1px solid #ff0000; color:#ff4444;">⚡ Activar Pulso Flash 416Hz</button>
        </div>

        <!-- ESTUDIO Z: CARGA DESDE GALERÍA -->
        <div class="card">
            <h3>🎛️ Cargar "Bandido.mp3" u Otro Tema</h3>
            <p style="font-size: 12px; color: #aaa;">Selecciona el archivo de audio real desde la memoria de tu teléfono.</p>
            
            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Título del Tema:</label>
            <input type="text" id="upload-title" placeholder="Ej. Bandido (Oficial)">
            
            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Artista:</label>
            <input type="text" id="upload-artist" value="Enyi el Científico">

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Frecuencia / Efecto:</label>
            <select id="effect-select">
                <option value="416Hz">416Hz (Identidad / Tríada)</option>
                <option value="7.83Hz">7.83Hz (Resonancia Schumann)</option>
                <option value="528Hz">528Hz (Reparación Ethereal)</option>
            </select>

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Portada (Imagen):</label>
            <input type="file" id="upload-cover" accept="image/*">

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Archivo de Audio (bandido.mp3):</label>
            <input type="file" id="upload-media" accept="audio/*">

            <button id="publish-btn">🚀 Subir y Fijar en el Sistema Z</button>
        </div>

        <!-- MURO / FEED -->
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

        function loadFeed() {
            let saved = JSON.parse(localStorage.getItem('sistema_z_tracks') || '[]');
            const feed = document.getElementById('pro-feed');
            feed.innerHTML = '';
            
            if (saved.length === 0) {
                feed.innerHTML = '<div class="card" style="text-align:center; color:#888; font-size:13px;">No hay temas cargados aún. Usa el formulario de arriba para subir tu <strong>bandido.mp3</strong> desde el teléfono.</div>';
                return;
            }

            saved.forEach(track => renderCard(track));
        }

        function handlePublish(e) {
            e.preventDefault();
            const title = document.getElementById('upload-title').value.trim() || 'Bandido';
            const artist = document.getElementById('upload-artist').value.trim() || 'Enyi el Científico';
            const effect = document.getElementById('effect-select').value;
            const mediaInput = document.getElementById('upload-media');
            const coverInput = document.getElementById('upload-cover');

            if (!mediaInput.files || mediaInput.files.length === 0) {
                alert('⚠️ Selecciona tu archivo bandido.mp3 antes de publicar.');
                return;
            }

            const mediaFile = mediaInput.files[0];
            const coverFile = coverInput.files && coverInput.files[0] ? coverInput.files[0] : null;

            const readerMedia = new FileReader();
            readerMedia.onload = function(evMedia) {
                const mediaUrl = evMedia.target.result;
                if (coverFile) {
                    const readerCover = new FileReader();
                    readerCover.onload = function(evCover) {
                        saveTrackData(title, artist, effect, evCover.target.result, mediaUrl);
                    };
                    readerCover.readAsDataURL(coverFile);
                } else {
                    saveTrackData(title, artist, effect, 'https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?w=500&q=80', mediaUrl);
                }
            };
            readerMedia.readAsDataURL(mediaFile);
        }

        function saveTrackData(title, artist, effect, coverUrl, mediaUrl) {
            const embedCode = `<iframe src="https://meygey.github.io/Sistema-z/" width="100%" height="150" style="background:#000;border:1px solid #ff0000;border-radius:6px;" title="${title}"></iframe>`;
            const track = { id: 't_' + Date.now(), title, artist, effect, coverUrl, mediaUrl, embedCode };

            let saved = JSON.parse(localStorage.getItem('sistema_z_tracks') || '[]');
            saved.unshift(track);
            localStorage.setItem('sistema_z_tracks', JSON.stringify(saved));

            loadFeed();
            document.getElementById('upload-title').value = '';
            document.getElementById('upload-media').value = '';
            document.getElementById('upload-cover').value = '';
            alert('✅ ¡Bandido.mp3 cargado y fijado con éxito en el Sistema Z!');
        }

        function renderCard(track) {
            const mediaHtml = `
                <div style="position:relative; width:100%; height:150px; background:#000; border-radius:6px; overflow:hidden; margin-top:8px;">
                    <img src="${track.coverUrl}" style="width:100%; height:100%; object-fit:cover; opacity:0.85;">
                    <div style="position:absolute; bottom:6px; left:6px; background:rgba(0,0,0,0.8); padding:3px 8px; font-size:10px; color:#ff0000; font-weight:bold; border-radius:3px;">🛡️ ${track.effect || '416Hz'}</div>
                </div>
                <audio controls src="${track.mediaUrl}" style="width:100%; margin-top:8px;"></audio>
            `;

            const card = document.createElement('div');
            card.className = 'card track-post-card';
            card.innerHTML = `
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:#ff2222; font-weight:bold; font-size:15px;">🔥 ${track.title}</span>
                    <span style="background:#220000; color:#ff4444; padding:2px 6px; border-radius:4px; font-size:10px;">${track.effect || 'Z-SYSTEM'}</span>
                </div>
                <div style="color:#aaa; font-size:12px; margin-top:2px;">Artista: <strong style="color:#fff;">${track.artist}</strong></div>
                ${mediaHtml}
                <div class="row-btns">
                    <button onclick="navigator.clipboard.writeText('${window.location.href}'); alert('🔗 ¡Enlace copiado!');" class="btn-action" style="flex:1; background:#1a1a1a; color:#fff; border:1px solid #444;">🔗 Compartir</button>
                    <button onclick="deleteTrack('${track.id}')" class="btn-action" style="background:#300; color:#ff6666; border:1px solid #ff0000;">🗑️ Borrar</button>
                </div>
                <div style="margin-top:8px;">
                    <span style="font-size:10px; color:#888;">Formato de Código (Embed):</span>
                    <textarea class="code-box" readonly>${track.embedCode}</textarea>
                </div>
            `;
            document.getElementById('pro-feed').appendChild(card);
        }

        function deleteTrack(id) {
            if (confirm('¿Eliminar este tema del sistema local?')) {
                let saved = JSON.parse(localStorage.getItem('sistema_z_tracks') || '[]');
                saved = saved.filter(t => t.id !== id);
                localStorage.setItem('sistema_z_tracks', JSON.stringify(saved));
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
                btn.innerText = '⚡ Activar Pulso Flash 416Hz';
                btn.style.background = '#220000';
            } else {
                btn.innerText = '🛑 Desactivar Pulso Flash';
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

print('¡AUDIO FALSO ELIMINADO Y SISTEMA LISTO PARA CARGAR BANDIDO.MP3 DESDE LA GALERÍA!')
