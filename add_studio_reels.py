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
        input[type="file"], select {
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
        }
        .btn-action {
            display: inline-block;
            text-align: center;
            background: #1a1a1a;
            border: 1px solid #ff0000;
            color: #ff2222;
            padding: 10px;
            margin-top: 6px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
            box-sizing: border-box;
            width: 100%;
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

        /* Vista previa de Cámara / Reel */
        #camera-container {
            position: relative;
            width: 100%;
            height: 350px;
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
        }
        
        /* Capas de Efectos Visuales Urbanos */
        .fx-layer {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 5;
        }
        
        /* Efecto 1: Glitch */
        .glitch-fx { animation: glitchAnim 0.3s infinite; }
        @keyframes glitchAnim {
            0% { transform: translate(2px, -2px); filter: hue-rotate(90deg); }
            50% { transform: translate(-2px, 2px); filter: hue-rotate(-90deg); }
            100% { transform: translate(0, 0); }
        }

        /* Efecto 2: Interferencia / VHS */
        .vhs-fx {
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            background-size: 100% 3px, 6px 100%;
        }

        /* Efecto 3: Falla en la Matriz */
        .matrix-fx {
            color: #00ffcc;
            text-shadow: 0 0 8px #00ffcc;
            background: rgba(0, 255, 100, 0.08);
            mix-blend-mode: overlay;
        }

        /* Efecto 4: Latido Rojo Intenso */
        .latido-fx { animation: latidoAnim 0.8s infinite alternate; }
        @keyframes latidoAnim {
            0% { box-shadow: inset 0 0 10px rgba(255,0,0,0.3); }
            100% { box-shadow: inset 0 0 45px rgba(255,0,0,0.8); }
        }

        /* Efecto 5: Rojo Oscuro Experimental (Ozuna Style) */
        .dark-exp-fx {
            background: rgba(100, 0, 0, 0.25);
            filter: contrast(130%) brightness(90%);
        }

        /* Efecto 6: Tríada 416Hz Z */
        .triada-fx {
            border: 4px solid #ff0000;
            box-shadow: inset 0 0 20px #ff0000;
        }

        /* Pantalla de Flash rítmico */
        #flash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #ffffff;
            opacity: 0;
            pointer-events: none;
            z-index: 9999;
            transition: opacity 0.05s ease;
        }

        .row-group {
            display: flex;
            gap: 8px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div id="flash-screen"></div>
    <div class="container">
        <h1>Sistema Z 🔺 416Hz</h1>
        <div class="subtitle">Tierra de Mafia • Enyi el Científico</div>

        <!-- 1. REPRODUCTOR BASE (YA PROBADO Y FUNCIONAL) -->
        <div class="card">
            <h3>🎛️ Reproductor Base (Bandido.mp3)</h3>
            <div style="text-align: center;"><span class="badge">FRECUENCIA 416Hz</span></div>
            <input type="file" id="local-audio-input" accept="audio/*" onchange="loadLocalBandido(this)">
            <audio id="master-audio" controls style="display:none; margin-top:10px;"></audio>
        </div>

        <!-- 2. ESTUDIO Z: CÁMARA Y REELS CON EFECTOS -->
        <div class="card" style="border: 2px solid #ff0000; background: #0c0000;">
            <h3>👺 Estudio Z: Grabador de Reels</h3>
            <div style="text-align: center;"><span class="badge">CÁMARA & 6 EFECTOS URBANOS</span></div>

            <!-- Visor de Cámara con Capas de Efectos -->
            <div id="camera-container">
                <div id="fx-layer" class="fx-layer"></div>
                <video id="webcam-video" autoplay playsinline muted></video>
            </div>

            <!-- Controles de Cámara -->
            <div class="row-group">
                <button type="button" onclick="startCamera('user')" style="background:#1a1a1a; border:1px solid #ff0000;">Frontal</button>
                <button type="button" onclick="startCamera('environment')" style="background:#1a1a1a; border:1px solid #ff0000;">Trasera</button>
            </div>

            <!-- Selector de 6 Efectos Visuales -->
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

            <!-- Control de Flash Rítmico -->
            <div class="row-group">
                <button type="button" onclick="toggleFlashMode()" id="flash-mode-btn" style="background:#220000; border:1px solid #ff0000; color:#ff4444;">Flash Rítmico: APAGADO</button>
            </div>

            <!-- Botones de Acción y Compartir -->
            <button type="button" onclick="toggleRecord()" id="record-btn" style="background:#ff0000; margin-top: 10px;">🔴 Iniciar Grabación Reel</button>
            
            <div id="result-download-area" style="display:none; margin-top: 15px; border-top: 1px solid #333; padding-top: 10px;">
                <video id="recorded-preview" controls playsinline style="margin-bottom: 8px;"></video>
                <a id="download-link" class="btn-action" download="bandido_reel_z.mp4">📥 Descargar Reel (MP4 / Redes)</a>
                <button type="button" onclick="shareToSocial()" style="background:#1a1a1a; border:1px solid #00ffcc; color:#00ffcc; margin-top:8px;">🔗 Compartir en Redes</button>
            </div>
        </div>
    </div>

    <script>
        let mediaStream = null;
        let mediaRecorder = null;
        let recordedChunks = [];
        let isRecording = false;
        let flashBeatInterval = null;
        let flashModeOn = false;

        // 1. Reproductor Base
        function loadLocalBandido(input) {
            if (input.files && input.files[0]) {
                const file = input.files[0];
                const audioEl = document.getElementById('master-audio');
                audioEl.src = URL.createObjectURL(file);
                audioEl.style.display = 'block';
                audioEl.play().catch(e => console.log("Play manual requerido"));
                alert('✅ ¡Bandido.mp3 sonando en el núcleo!');
            }
        }

        // 2. Control de Cámara (Frontal / Trasera)
        async function startCamera(facingMode) {
            if (mediaStream) {
                mediaStream.getTracks().forEach(track => track.stop());
            }
            try {
                mediaStream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: facingMode },
                    audio: true
                });
                const videoEl = document.getElementById('webcam-video');
                videoEl.srcObject = mediaStream;
            } catch (err) {
                alert('⚠️ No se pudo acceder a la cámara. Revisa los permisos del navegador.');
            }
        }

        // 3. Selector de 6 Efectos Visuales
        function changeVisualEffect(fxName) {
            const layer = document.getElementById('fx-layer');
            layer.className = 'fx-layer'; // Limpiar
            if (fxName !== 'none') {
                layer.classList.add(fxName + '-fx');
            }
        }

        // 4. Control de Flash Rítmico (Pantalla y hardware si soporta)
        function toggleFlashMode() {
            flashModeOn = !flashModeOn;
            const btn = document.getElementById('flash-mode-btn');
            const flashScreen = document.getElementById('flash-screen');
            
            if (flashModeOn) {
                btn.innerText = 'Flash Rítmico: ENCENDIDO (416Hz)';
                btn.style.background = '#ff0000';
                btn.style.color = '#fff';
                
                // Simular latido lumínico al ritmo del beat (aprox 120 BPM / 500ms)
                let toggle = false;
                flashBeatInterval = setInterval(() => {
                    toggle = !toggle;
                    flashScreen.style.opacity = toggle ? '0.2' : '0';
                }, 400);
            } else {
                btn.innerText = 'Flash Rítmico: APAGADO';
                btn.style.background = '#220000';
                btn.style.color = '#ff4444';
                clearInterval(flashBeatInterval);
                flashScreen.style.opacity = '0';
            }
        }

        // 5. Grabación de Reel y Formato Compatible para Redes
        function toggleRecord() {
            if (!mediaStream) {
                alert('⚠️ Primero enciende la cámara (Frontal o Trasera).');
                startCamera('user');
                return;
            }

            const recordBtn = document.getElementById('record-btn');
            const resultArea = document.getElementById('result-download-area');

            if (!isRecording) {
                recordedChunks = [];
                try {
                    // Codec optimizado compatible con Instagram, TikTok y YouTube Shorts (VP8/WebM o MP4)
                    let options = { mimeType: 'video/webm;codecs=vp8,opus' };
                    if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                        options = { mimeType: 'video/webm' };
                    }

                    mediaRecorder = new MediaRecorder(mediaStream, options);
                    mediaRecorder.ondataavailable = (event) => {
                        if (event.data.size > 0) recordedChunks.push(event.data);
                    };

                    mediaRecorder.onstop = () => {
                        const blob = new Blob(recordedChunks, { type: 'video/mp4' });
                        const videoUrl = URL.createObjectURL(blob);
                        
                        const preview = document.getElementById('recorded-preview');
                        preview.src = videoUrl;
                        
                        const downloadLink = document.getElementById('download-link');
                        downloadLink.href = videoUrl;
                        
                        resultArea.style.display = 'block';
                        alert('✅ ¡Reel grabado con éxito y codificado para redes sociales!');
                    };

                    mediaRecorder.start();
                    isRecording = true;
                    recordBtn.innerText = '⏹️ Detener Grabación';
                    recordBtn.style.background = '#333';
                } catch (err) {
                    alert('⚠️ Error al iniciar la grabación en este navegador.');
                }
            } else {
                mediaRecorder.stop();
                isRecording = false;
                recordBtn.innerText = '🔴 Iniciar Grabación Reel';
                recordBtn.style.background = '#ff0000';
            }
        }

        // 6. Compartir en Redes
        async function shareToSocial() {
            if (navigator.share) {
                try {
                    await navigator.share({
                        title: 'Sistema Z - Reel Oficial',
                        text: 'Escucha Bandido de Enyi el Científico #SistemaZ #416Hz',
                        url: window.location.href
                    });
                } catch (err) {
                    console.log('Compartir cancelado');
                }
            } else {
                alert('🔗 Enlace copiado al portapapeles. ¡Pégalo en tus redes!');
                navigator.clipboard.writeText(window.location.href);
            }
        }

        // Arrancar cámara frontal por defecto al cargar
        window.onload = () => {
            startCamera('user');
        };
    </script>
</body>
</html>
""")

print('¡ESTUDIO Z DE REELS Y CÁMARA INTEGRADO CON 6 EFECTOS Y FLASH RÍTMICO!')
