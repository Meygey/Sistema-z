with open('index.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Z | Bóveda & Estudio de Reels</title>
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
        audio, video {
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
            border-radius: 6px;
            cursor: pointer;
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

        /* ESTUDIO Z: CÁMARA Y EFECTOS */
        #camera-container {
            position: relative;
            width: 100%;
            height: 340px;
            background: #000;
            border: 2px solid #ff0000;
            border-radius: 8px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        #webcam-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            margin-top: 0;
        }
        .fx-layer {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 5;
        }
        .glitch-fx { animation: glitchAnim 0.3s infinite; }
        @keyframes glitchAnim {
            0% { transform: translate(2px, -2px); filter: hue-rotate(90deg); }
            50% { transform: translate(-2px, 2px); filter: hue-rotate(-90deg); }
            100% { transform: translate(0, 0); }
        }
        .vhs-fx {
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            background-size: 100% 3px, 6px 100%;
        }
        .matrix-fx {
            color: #00ffcc;
            text-shadow: 0 0 8px #00ffcc;
            background: rgba(0, 255, 100, 0.08);
            mix-blend-mode: overlay;
        }
        .latido-fx { animation: latidoAnim 0.8s infinite alternate; }
        @keyframes latidoAnim {
            0% { box-shadow: inset 0 0 10px rgba(255,0,0,0.3); }
            100% { box-shadow: inset 0 0 45px rgba(255,0,0,0.8); }
        }
        .dark-exp-fx {
            background: rgba(100, 0, 0, 0.25);
            filter: contrast(130%) brightness(90%);
        }
        .triada-fx {
            border: 4px solid #ff0000;
            box-shadow: inset 0 0 20px #ff0000;
        }
        #flash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #ffffff;
            opacity: 0;
            pointer-events: none;
            z-index: 9999;
            transition: opacity 0.05s ease;
        }
    </style>
</head>
<body>
    <div id="flash-screen"></div>
    <div class="container">
        <header>
            <h1>Sistema Z 🔺 Bóveda & Estudio</h1>
            <div class="subtitle">Tierra de Mafia • Sello Descentralizado</div>
        </header>

        <!-- 1. PANEL DE SUBIDA CON PORTADA Y PERSISTENCIA INDEXEDDB -->
        <div class="card">
            <h3>🚀 Subida Oficial de Temas</h3>
            <div style="text-align: center;"><span class="badge">PROTECCIÓN Y COPYRIGHT Z</span></div>
            
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

        <!-- 2. ESTUDIO Z: CÁMARA, 6 EFECTOS Y AUDIO DE SISTEMA -->
        <div class="card" style="border: 2px solid #ff0000; background: #0c0000;">
            <h3>👺 Estudio Z: Grabador de Reels</h3>
            <div style="text-align: center;"><span class="badge">CÁMARA DUAL & AUDIO DE SISTEMA</span></div>

            <div id="camera-container">
                <div id="fx-layer" class="fx-layer"></div>
                <video id="webcam-video" autoplay playsinline muted></video>
            </div>

            <div class="btn-row" style="margin-bottom: 10px;">
                <button type="button" onclick="startCamera('user')" style="background:#1a1a1a; border:1px solid #ff0000; padding:8px;">Frontal</button>
                <button type="button" onclick="startCamera('environment')" style="background:#1a1a1a; border:1px solid #ff0000; padding:8px;">Trasera</button>
            </div>

            <label style="font-size: 11px; color: #ff4444; font-weight: bold; display: block;">Efecto Visual Urbano:</label>
            <select id="effect-selector" onchange="changeVisualEffect(this.value)">
                <option value="none">Normal (Sin Efecto)</option>
                <option value="glitch">1. Glitch Cyber</option>
                <option value="vhs">2. Interferencia / VHS</option>
                <option value="matrix">3. Falla en la Matriz</option>
                <option value="latido">4. Latido Subconsciente</option>
                <option value="dark-exp">5. Dark Experimental</option>
                <option value="triada">6. Tríada 416Hz</option>
            </select>

            <label style="font-size: 11px; color: #ff4444; font-weight: bold; display: block; margin-top: 8px;">Tema Musical de Fondo (Audio de Sistema):</label>
            <select id="reel-track-select">
                <option value="">-- Sin música (Solo Micrófono) --</option>
            </select>

            <button type="button" onclick="toggleFlashMode()" id="flash-mode-btn" style="background:#220000; border:1px solid #ff0000; color:#ff4444; margin-top: 8px;">Flash Rítmico: APAGADO</button>

            <button type="button" onclick="toggleRecord()" id="record-btn" style="background:#ff0000; margin-top: 12px;">🔴 Iniciar Grabación Reel</button>
            
            <div id="result-download-area" style="display:none; margin-top: 15px; border-top: 1px solid #333; padding-top: 10px;">
                <video id="recorded-preview" controls playsinline style="width:100%; border-radius:6px; margin-bottom: 8px;"></video>
                <a id="download-reel-link" class="btn-dl" download="reel_z_sistema.mp4" style="display:block; padding:10px;">📥 Descargar Reel MP4 (Redes)</a>
            </div>
        </div>

        <!-- 3. CATÁLOGO PERMANENTE DE LA BÓVEDA -->
        <div class="card">
            <h3>🎧 Catálogo Global Activo (Bóveda)</h3>
            <div id="vault-playlist">
                <p style="color:#888; font-size:12px; text-align:center;">Cargando bóveda segura...</p>
            </div>
        </div>

        <!-- 4. MURO DE REELS GRABADOS -->
        <div class="card">
            <h3>📂 Muro de Reels Grabados</h3>
            <div id="reels-vault-list">
                <p style="color:#888; font-size:12px; text-align:center;">No hay reels grabados todavía.</p>
            </div>
        </div>
    </div>

    <script>
        let db;
        const dbName = "SistemaZ_Vault_DB";
        const storeName = "tracks";
        const reelsStoreName = "reels";

        let mediaStream = null;
        let mediaRecorder = null;
        let recordedChunks = [];
        let isRecording = false;
        let flashBeatInterval = null;
        let flashModeOn = false;

        let audioCtx = null;
        let activeAudioElement = null;

        // Inicializar IndexedDB con soporte para Tracks y Reels
        const request = indexedDB.open(dbName, 2);

        request.onerror = function(event) {
            console.error("Error al abrir IndexedDB", event);
        };

        request.onsuccess = function(event) {
            db = event.target.result;
            loadVaultTracks();
            loadReelsVault();
        };

        request.onupgradeneeded = function(event) {
            db = event.target.result;
            if (!db.objectStoreNames.contains(storeName)) {
                db.createObjectStore(storeName, { keyPath: "id" });
            }
            if (!db.objectStoreNames.contains(reelsStoreName)) {
                db.createObjectStore(reelsStoreName, { keyPath: "id" });
            }
        };

        // --- GESTIÓN DE BÓVEDA (TRACKS) ---
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
        }

        function loadVaultTracks() {
            if (!db) return;
            const container = document.getElementById('vault-playlist');
            const reelSelect = document.getElementById('reel-track-select');
            
            container.innerHTML = '';
            reelSelect.innerHTML = '<option value="">-- Sin música (Solo Micrófono) --</option>';

            const transaction = db.transaction([storeName], "readonly");
            const store = transaction.objectStore(storeName);
            const req = store.getAll();

            req.onsuccess = function(event) {
                const tracks = event.target.result;

                if (tracks.length === 0) {
                    container.innerHTML = '<p style="color:#888; font-size:12px; text-align:center;">La bóveda está vacía. Sube tu primer tema arriba.</p>';
                    return;
                }

                tracks.reverse().forEach(track => {
                    // Agregar opción al selector de reels
                    const opt = document.createElement('option');
                    opt.value = track.audioUrl;
                    opt.text = `${track.title} - ${track.artist} (${track.freq})`;
                    reelSelect.appendChild(opt);

                    // Renderizar tarjeta en la bóveda
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
                            <button type="button" class="btn-del" onclick="deleteTrackFromVault('${track.id}')">🗑️ Eliminar</button>
                        </div>
                    `;
                    container.appendChild(div);
                });
            };
        }

        function deleteTrackFromVault(id) {
            if (confirm('¿Estás seguro de eliminar este tema de la bóveda soberana?')) {
                const transaction = db.transaction([storeName], "readwrite");
                const store = transaction.objectStore(storeName);
                const req = store.delete(id);

                req.onsuccess = function() {
                    loadVaultTracks();
                    alert('🗑️ Tema eliminado correctamente.');
                };
            }
        }

        // --- ESTUDIO Z: CÁMARA Y EFECTOS ---
        window.onload = () => {
            startCamera('user');
        };

        async function startCamera(facingMode) {
            if (mediaStream) {
                mediaStream.getTracks().forEach(track => track.stop());
            }
            try {
                mediaStream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: facingMode },
                    audio: true
                });
                document.getElementById('webcam-video').srcObject = mediaStream;
            } catch (err) {
                alert('⚠️ No se pudo acceder a la cámara. Revisa los permisos.');
            }
        }

        function changeVisualEffect(fxName) {
            const layer = document.getElementById('fx-layer');
            layer.className = 'fx-layer';
            if (fxName !== 'none') {
                layer.classList.add(fxName + '-fx');
            }
        }

        function toggleFlashMode() {
            flashModeOn = !flashModeOn;
            const btn = document.getElementById('flash-mode-btn');
            const flashScreen = document.getElementById('flash-screen');
            
            if (flashModeOn) {
                btn.innerText = 'Flash Rítmico: ENCENDIDO';
                btn.style.background = '#ff0000';
                btn.style.color = '#fff';
                let toggle = false;
                flashBeatInterval = setInterval(() => {
                    toggle = !toggle;
                    flashScreen.style.opacity = toggle ? '0.25' : '0';
                }, 400);
            } else {
                btn.innerText = 'Flash Rítmico: APAGADO';
                btn.style.background = '#220000';
                btn.style.color = '#ff4444';
                clearInterval(flashBeatInterval);
                flashScreen.style.opacity = '0';
            }
        }

        // --- GRABACIÓN DE REEL CON AUDIO DE SISTEMA (WEB AUDIO API) ---
        async function toggleRecord() {
            if (!mediaStream) {
                alert('⚠️ Enciende la cámara primero.');
                return;
            }

            const recordBtn = document.getElementById('record-btn');
            const resultArea = document.getElementById('result-download-area');
            const selectedAudioUrl = document.getElementById('reel-track-select').value;

            if (!isRecording) {
                recordedChunks = [];
                try {
                    if (!audioCtx) {
                        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                    }
                    if (audioCtx.state === 'suspended') {
                        await audioCtx.resume();
                    }

                    let dest = audioCtx.createMediaStreamDestination();

                    // 1. Conectar micrófono
                    let micSource = audioCtx.createMediaStreamSource(mediaStream);
                    micSource.connect(dest);

                    // 2. Conectar audio de sistema si se seleccionó un tema
                    if (selectedAudioUrl) {
                        if (activeAudioElement) {
                            activeAudioElement.pause();
                        }
                        activeAudioElement = new Audio(selectedAudioUrl);
                        activeAudioElement.crossOrigin = "anonymous";
                        activeAudioElement.currentTime = 0;
                        await activeAudioElement.play();

                        let trackSource = audioCtx.createMediaElementSource(activeAudioElement);
                        trackSource.connect(dest);
                        trackSource.connect(audioCtx.destination); // Escuchar en cornetas
                    }

                    // Fusionar video de cámara con audio mixto
                    let combinedStream = new MediaStream([
                        ...mediaStream.getVideoTracks(),
                        ...dest.stream.getAudioTracks()
                    ]);

                    let options = { mimeType: 'video/webm;codecs=vp8,opus' };
                    if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                        options = { mimeType: 'video/webm' };
                    }

                    mediaRecorder = new MediaRecorder(combinedStream, options);
                    mediaRecorder.ondataavailable = (e) => { if (e.data.size > 0) recordedChunks.push(e.data); };
                    
                    mediaRecorder.onstop = () => {
                        const blob = new Blob(recordedChunks, { type: 'video/mp4' });
                        const videoUrl = URL.createObjectURL(blob);
                        
                        document.getElementById('recorded-preview').src = videoUrl;
                        document.getElementById('download-reel-link').href = videoUrl;
                        resultArea.style.display = 'block';

                        saveReelToVault('Reel Z - ' + new Date().toLocaleTimeString(), videoUrl);
                        alert('✅ ¡Reel grabado con éxito y audio de sistema incluido!');
                    };

                    mediaRecorder.start();
                    isRecording = true;
                    recordBtn.innerText = '⏹️ Detener Grabación (Grabando...)';
                    recordBtn.style.background = '#333';
                } catch (err) {
                    console.error(err);
                    alert('⚠️ Error al iniciar la grabación con audio interno.');
                }
            } else {
                mediaRecorder.stop();
                if (activeAudioElement) {
                    activeAudioElement.pause();
                }
                isRecording = false;
                recordBtn.innerText = '🔴 Iniciar Grabación Reel';
                recordBtn.style.background = '#ff0000';
            }
        }

        function saveReelToVault(title, videoUrl) {
            const reelData = {
                id: 'reel_' + Date.now(),
                title,
                videoUrl,
                date: new Date().toLocaleDateString()
            };

            const transaction = db.transaction([reelsStoreName], "readwrite");
            const store = transaction.objectStore(reelsStoreName);
            store.add(reelData);

            loadReelsVault();
        }

        function loadReelsVault() {
            if (!db) return;
            const container = document.getElementById('reels-vault-list');
            container.innerHTML = '';

            const transaction = db.transaction([reelsStoreName], "readonly");
            const store = transaction.objectStore(reelsStoreName);
            const req = store.getAll();

            req.onsuccess = function(event) {
                const reels = event.target.result;

                if (reels.length === 0) {
                    container.innerHTML = '<p style="color:#888; font-size:12px; text-align:center;">No hay reels grabados todavía.</p>';
                    return;
                }

                reels.reverse().forEach(reel => {
                    const div = document.createElement('div');
                    div.className = 'track-item';
                    div.innerHTML = `
                        <div style="color:#ff4444; font-weight:bold; font-size:13px; margin-bottom:5px;">🔥 ${reel.title}</div>
                        <video controls src="${reel.videoUrl}" style="width:100%; max-height:200px; object-fit:cover; border-radius:4px;"></video>
                        <a href="${reel.videoUrl}" download="reel_z.mp4" class="btn-dl" style="margin-top:6px;">📥 Descargar MP4</a>
                    `;
                    container.appendChild(div);
                });
            };
        }
    </script>
</body>
</html>
""")

print('¡FASE 2 COMPLETADA: ESTUDIO Z DE REELS, CÁMARA DUAL, 6 EFECTOS Y AUDIO DE SISTEMA!')
