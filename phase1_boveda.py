with open('index.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Z | Bóveda Infinita & Copyright</title>
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
            max-width: 550px;
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
            text-align: center;
        }
        input[type="file"], input[type="text"], select {
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
        audio {
            width: 100%;
            border-radius: 6px;
            margin-top: 8px;
        }
        .badge {
            display: inline-block;
            background: #220000;
            color: #ff4444;
            border: 1px solid #ff0000;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .track-item {
            background: #111;
            border: 1px solid #333;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 15px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .track-header {
            display: flex;
            gap: 12px;
            align-items: center;
        }
        .track-cover {
            width: 70px;
            height: 70px;
            object-fit: cover;
            border-radius: 6px;
            border: 1px solid #ff0000;
        }
        .track-info {
            flex-grow: 1;
        }
        .track-title {
            color: #ff2222;
            font-weight: bold;
            font-size: 15px;
            margin: 0 0 4px 0;
        }
        .track-artist {
            color: #aaa;
            font-size: 12px;
            margin: 0 0 4px 0;
        }
        .copyright-box {
            background: #160000;
            border: 1px dashed #ff0000;
            padding: 6px 8px;
            border-radius: 4px;
            font-size: 10px;
            color: #ff8888;
            font-family: monospace;
            margin-top: 5px;
        }
        .btn-row {
            display: flex;
            gap: 8px;
            margin-top: 5px;
        }
        .btn-del {
            background: #300;
            color: #ff6666;
            border: 1px solid #ff0000;
            padding: 6px;
            font-size: 11px;
            flex: 1;
        }
        .btn-dl {
            background: #1a1a1a;
            color: #00ffcc;
            border: 1px solid #00ffcc;
            padding: 6px;
            font-size: 11px;
            flex: 1;
            text-decoration: none;
            text-align: center;
            border-radius: 6px;
            font-weight: bold;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Sistema Z 🔺 Bóveda 416Hz</h1>
            <div class="subtitle">Tierra de Mafia • Sello Descentralizado</div>
        </header>

        <!-- PANEL DE SUBIDA CON PORTADA Y PERSISTENCIA INDEXEDDB -->
        <div class="card">
            <h3>🚀 Subida Oficial de Temas</h3>
            <div style="text-align: center;"><span class="badge">PROTECCIÓN Y COPYRIGHT AUTOMÁTICO</span></div>
            
            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Título del Tema:</label>
            <input type="text" id="input-title" placeholder="Ej. La Elegida, Bandido...">

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Artista / Autor:</label>
            <input type="text" id="input-artist" placeholder="Ej. Enyi el Científico">

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Frecuencia / Sello:</label>
            <select id="input-freq">
                <option value="416Hz">416Hz (Identidad / Tríada Z)</option>
                <option value="7.83Hz">7.83Hz (Resonancia Schumann)</option>
                <option value="528Hz">528Hz (Reparación Ethereal)</option>
            </select>

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Imagen de Portada:</label>
            <input type="file" id="input-cover" accept="image/*">

            <label style="font-size: 11px; color: #ff4444; font-weight: bold;">Archivo de Audio (MP3):</label>
            <input type="file" id="input-audio" accept="audio/*">

            <button type="button" onclick="uploadTrackToVault()">🔥 Registrar y Subir a la Bóveda</button>
        </div>

        <!-- LISTA PERMANENTE DE TEMAS -->
        <div class="card">
            <h3>🎧 Catálogo Global Activo (Persistente)</h3>
            <div id="vault-playlist">
                <p style="color:#888; font-size:12px; text-align:center;">Cargando bóveda segura...</p>
            </div>
        </div>
    </div>

    <script>
        // Configuración de IndexedDB para persistencia absoluta (Anti-desaparición)
        let db;
        const dbName = "SistemaZ_Vault_DB";
        const storeName = "tracks";

        const request = indexedDB.open(dbName, 1);

        request.onerror = function(event) {
            console.error("Error al abrir IndexedDB", event);
            alert("⚠️ Error crítico de almacenamiento local.");
        };

        request.onsuccess = function(event) {
            db = event.target.result;
            loadVaultTracks();
        };

        request.onupgradeneeded = function(event) {
            db = event.target.result;
            if (!db.objectStoreNames.contains(storeName)) {
                db.createObjectStore(storeName, { keyPath: "id" });
            }
        };

        // Subir tema a la bóveda
        function uploadTrackToVault() {
            const title = document.getElementById('input-title').value.trim();
            const artist = document.getElementById('input-artist').value.trim();
            const freq = document.getElementById('input-freq').value;
            const coverFile = document.getElementById('input-cover').files[0];
            const audioFile = document.getElementById('input-audio').files[0];

            if (!title || !audioFile) {
                alert('⚠️ Debes colocar al menos el título y el archivo MP3 del tema.');
                return;
            }

            const reader = new FileReader();
            reader.onload = function(eAudio) {
                const audioData = eAudio.target.result;

                if (coverFile) {
                    const readerCover = new FileReader();
                    readerCover.onload = function(eCover) {
                        saveToDB(title, artist || 'Enyi el Científico', freq, eCover.target.result, audioData);
                    };
                    readerCover.readAsDataURL(coverFile);
                } else {
                    // Portada por defecto del Sistema Z (Negro/Rojo)
                    saveToDB(title, artist || 'Enyi el Científico', freq, 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" style="background:#000"><text x="50%" y="50%" fill="%23ff0000" font-size="20" font-weight="bold" dominant-baseline="middle" text-anchor="middle">Z</text></svg>', audioData);
                }
            };
            reader.readAsDataURL(audioFile);
        }

        function saveToDB(title, artist, freq, coverUrl, audioUrl) {
            const trackId = 'z_' + Date.now();
            const copyrightHash = 'Z-AUTH-416-' + Math.random().toString(36).substring(2, 9).toUpperCase() + '-' + Date.now().toString().slice(-4);
            
            const trackData = {
                id: trackId,
                title,
                artist,
                freq,
                coverUrl,
                audioUrl,
                copyright: copyrightHash,
                date: new Date().toLocaleDateString()
            };

            const transaction = db.transaction([storeName], "readwrite");
            const store = transaction.objectStore(storeName);
            const req = store.add(trackData);

            req.onsuccess = function() {
                document.getElementById('input-title').value = '';
                document.getElementById('input-artist').value = '';
                document.getElementById('input-cover').value = '';
                document.getElementById('input-audio').value = '';
                loadVaultTracks();
                alert('✅ ¡Tema registrado en la Bóveda con su Sello de Copyright Z!');
            };

            req.onerror = function() {
                alert('⚠️ Error al guardar el archivo en la base de datos segura.');
            };
        }

        // Cargar temas desde IndexedDB
        function loadVaultTracks() {
            if (!db) return;
            const container = document.getElementById('vault-playlist');
            container.innerHTML = '';

            const transaction = db.transaction([storeName], "readonly");
            const store = transaction.objectStore(storeName);
            const req = store.getAll();

            req.onsuccess = function(event) {
                const tracks = event.target.result;

                if (tracks.length === 0) {
                    container.innerHTML = '<p style="color:#888; font-size:12px; text-align:center;">La bóveda está vacía. Sube tu primer tema arriba.</p>';
                    return;
                }

                // Ordenar del más nuevo al más antiguo
                tracks.reverse().forEach(track => {
                    const div = document.createElement('div');
                    div.className = 'track-item';
                    div.innerHTML = `
                        <div class="track-header">
                            <img src="${track.coverUrl}" class="track-cover" alt="Cover">
                            <div class="track-info">
                                <div class="track-title">🔥 ${track.title}</div>
                                <div class="track-artist">${track.artist} • <span style="color:#ff4444;">${track.freq}</span></div>
                                <div class="copyright-box">🛡️ Copyright Z: ${track.copyright}</div>
                            </div>
                        </div>
                        <audio controls src="${track.audioUrl}"></audio>
                        <div class="btn-row">
                            <a href="${track.audioUrl}" download="${track.title}.mp3" class="btn-dl">📥 Descargar MP3</a>
                            <button type="button" class="btn-del" onclick="deleteTrackFromVault('${track.id}')">🗑️ Eliminar Tema</button>
                        </div>
                    `;
                    container.appendChild(div);
                });
            };
        }

        // Eliminar tema (Control total del administrador/creador)
        function deleteTrackFromVault(id) {
            if (confirm('¿Estás seguro de eliminar este tema de la bóveda soberana?')) {
                const transaction = db.transaction([storeName], "readwrite");
                const store = transaction.objectStore(storeName);
                const req = store.delete(id);

                req.onsuccess = function() {
                    loadVaultTracks();
                    alert('🗑️ Tema eliminado correctamente de la red.');
                };
            }
        }
    </script>
</body>
</html>
""")

print('¡FASE 1 COMPLETADA: BÓVEDA INFINITA CON INDEXEDDB, PORTADAS Y COPYRIGHT Z!')
