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
            padding: 20px;
            text-align: center;
        }
        .container {
            max-width: 500px;
            margin: 40px auto;
        }
        h1 {
            color: #ff0000;
            font-size: 26px;
            margin: 5px 0;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .subtitle {
            color: #888;
            font-size: 13px;
            margin-bottom: 30px;
        }
        .card {
            background: #0a0a0a;
            border: 2px solid #ff0000;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 25px rgba(255, 0, 0, 0.25);
            text-align: left;
        }
        .card h3 {
            color: #ff2222;
            margin-top: 0;
            font-size: 18px;
            text-align: center;
        }
        input[type="file"] {
            background: #111;
            border: 1px solid #444;
            color: #fff;
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
            border-radius: 6px;
            margin: 10px 0 15px 0;
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
        }
        button:hover {
            background: #cc0000;
        }
        audio {
            width: 100%;
            margin-top: 15px;
            border-radius: 6px;
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
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sistema Z 🔺 416Hz</h1>
        <div class="subtitle">Tierra de Mafia • Enyi el Científico</div>

        <div class="card">
            <h3>🎛️ Núcleo Z: Reproductor Base</h3>
            <div style="text-align: center;">
                <span class="badge">FRECUENCIA 416Hz ACTIVA</span>
            </div>
            
            <p style="font-size: 13px; color: #aaa; text-align: center; margin-top: 5px;">
                Carga tu archivo <strong>bandido.mp3</strong> desde el almacenamiento de tu teléfono para iniciar el motor.
            </p>

            <label style="font-size: 11px; color: #ff4444; font-weight: bold; display: block;">Seleccionar "bandido.mp3":</label>
            <input type="file" id="local-audio-input" accept="audio/*" onchange="loadLocalBandido(this)">

            <div id="player-container" style="display: none; margin-top: 15px; border-top: 1px solid #222; padding-top: 15px; text-align: center;">
                <div style="color: #fff; font-weight: bold; font-size: 15px; margin-bottom: 8px;">🔥 Bandido (Oficial)</div>
                <audio id="master-audio" controls></audio>
            </div>
        </div>
    </div>

    <script>
        function loadLocalBandido(input) {
            if (input.files && input.files[0]) {
                const file = input.files[0];
                const audioUrl = URL.createObjectURL(file);
                
                const audioEl = document.getElementById('master-audio');
                audioEl.src = audioUrl;
                
                document.getElementById('player-container').style.display = 'block';
                audioEl.play().catch(e => console.log("Autoplay bloqueado por navegador, requiere toque manual."));
                
                alert('✅ ¡Bandido.mp3 cargado con éxito en el reproductor base!');
            }
        }
    </script>
</body>
</html>
""")

print('¡SISTEMA REINICIADO DESDE CERO: SOLO REPRODUCTOR BASE CON BANDIDO.MP3!')
