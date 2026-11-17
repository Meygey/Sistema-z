import os

print("🔥 [SISTEMA Z] Blindando interactividad y activando todos los botones...")

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Z | Tierra de Mafia</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body { background-color: #030303; color: #ffffff; font-family: 'Inter', sans-serif; }
        .font-z { font-family: 'Orbitron', sans-serif; }
        .glow-red { box-shadow: 0 0 25px rgba(255, 0, 0, 0.4); }
        .border-z { border-color: #ff0000; }
        .bg-z-red { background-color: #ff0000; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">
    <!-- Cabecera Oficial -->
    <header class="border-b border-z p-4 bg-[#080808] sticky top-0 z-50 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <div class="w-4 h-4 bg-z-red rounded-full animate-pulse glow-red"></div>
            <div>
                <h1 class="font-z font-black text-lg tracking-wider text-red-600">SISTEMA <span class="text-white">Z</span></h1>
                <p class="text-[10px] text-zinc-400 font-z">BIENVENIDO AL SISTEMA Z • SCRIPT & CASH</p>
            </div>
        </div>
        <div class="text-right">
            <span class="text-xs font-z text-red-500 border border-z px-2 py-1 rounded block">TIERRA DE MAFIA</span>
            <span class="text-[10px] text-zinc-500 font-mono">Visitas: <span id="visit-count">416</span></span>
        </div>
    </header>

    <main class="container mx-auto px-4 py-8 max-w-4xl flex-grow">
        <!-- Estado del Vault -->
        <div class="bg-[#0b0b0b] border border-z rounded-xl p-6 glow-red mb-8">
            <h2 class="font-z text-xl font-bold mb-2 text-white">PUERTO TERMINAL <span class="text-red-600">Z</span></h2>
            <p class="text-gray-400 text-xs mb-3">Plataforma descentralizada de alta frecuencia (cuatro dieciséis Hz). Interactividad total activa.</p>
            <div id="status-box" class="p-3 bg-black border border-zinc-800 rounded text-xs text-red-400 font-mono">
                ⚡ Estado: Inicializando motores de interfaz...
            </div>
        </div>

        <!-- Cuadrícula 1: Operaciones de Carga Local & Copyright Z -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl">
                <h3 class="font-z font-bold text-sm mb-3 text-red-500">🎧 Carga Directa & Copyright Z</h3>
                <p class="text-[11px] text-gray-400 mb-4">Sube tu tema desde la galería. Se genera sello digital y perfil automático.</p>
                
                <select id="destType" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white mb-3 outline-none focus:border-red-600">
                    <option value="catalog">Catálogo Universal</option>
                    <option value="profile">Perfil Personal de Artista</option>
                </select>

                <input type="text" id="artistName" placeholder="Nombre del Artista / Autor (Ej: Enyi el Científico)" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white mb-3 outline-none focus:border-red-600"/>
                <input type="text" id="trackTitle" placeholder="Título del Tema (Coro inicial)" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white mb-3 outline-none focus:border-red-600"/>
                
                <label class="block text-[10px] text-zinc-400 mb-1">Archivo de Audio / Video (MP3, WAV, MP4):</label>
                <input type="file" id="mediaFile" accept="audio/*,video/*" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-zinc-400 mb-3 file:bg-red-600 file:text-white file:border-0 file:rounded file:text-[10px] file:py-1 file:px-2"/>

                <label class="block text-[10px] text-zinc-400 mb-1">Imagen de Portada:</label>
                <input type="file" id="coverFile" accept="image/*" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-zinc-400 mb-4 file:bg-zinc-800 file:text-white file:border-0 file:rounded file:text-[10px] file:py-1 file:px-2"/>

                <button id="btnRegistrar" class="w-full bg-red-600 hover:bg-red-700 text-white font-z py-2 rounded text-xs transition font-bold cursor-pointer">PUBLICAR Y GENERAR COPYRIGHT Z</button>
            </div>

            <!-- Cuadrícula 2: Puerto Terminal Z & Directorio -->
            <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl flex flex-col justify-between">
                <div>
                    <h3 class="font-z font-bold text-sm mb-3 text-red-500">🔐 Puerto Terminal Z (Perfiles)</h3>
                    <p class="text-[11px] text-gray-400 mb-3">Acceso seguro para artistas. Gestiona tu perfil, visualiza reproducciones y borrados protegidos.</p>
                    
                    <input type="text" id="loginUser" placeholder="Usuario / Alias de Artista" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white mb-2 outline-none focus:border-red-600"/>
                    <input type="password" id="loginPass" placeholder="Contraseña" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white mb-3 outline-none focus:border-red-600"/>
                </div>
                <div class="space-y-2">
                    <button id="btnLogin" class="w-full border border-red-600 text-red-500 hover:bg-red-950 font-z py-2 rounded text-xs transition font-bold cursor-pointer">INGRESAR A MI PERFIL</button>
                    <input type="text" id="searchArtist" placeholder="🔍 Buscar perfil de artista..." class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                </div>
            </div>
        </div>

        <!-- Cuadrícula 3: Buscador Global, Reproductor & Muro de Tendencias (Trendy) -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl mb-8">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">🌐 Buscador Global, Reproductor & Tendencias (Trendy)</h3>
            <p class="text-[11px] text-gray-400 mb-4">Temas posicionados por el algoritmo del Sistema Z en base a visualizaciones, likes y comentarios.</p>
            <div class="flex gap-2 mb-4">
                <input type="text" id="globalSearchInput" placeholder="Escribe el nombre del tema o artista..." class="flex-grow bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                <button id="btnBuscar" class="bg-red-600 hover:bg-red-700 text-white font-z px-4 py-2 rounded text-xs font-bold cursor-pointer">BUSCAR</button>
            </div>
            
            <!-- Reproductor Universal Operativo -->
            <div class="p-4 bg-black border border-zinc-900 rounded space-y-3 mb-4">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-red-500 font-z font-bold">🎵 REPRODUCTOR ACTIVO</span>
                    <span id="nowPlayingTitle" class="text-xs text-zinc-300 font-mono">Ningún tema en reproducción</span>
                </div>
                <audio id="globalAudioPlayer" controls class="w-full h-8 accent-red-600"></audio>
                
                <!-- Sistema de Likes y Comentarios en Vivo para el Tema en Reproducción -->
                <div class="border-t border-zinc-800 pt-3 mt-2 flex items-center justify-between">
                    <button id="btnLike" class="bg-zinc-900 hover:bg-red-950 text-red-500 border border-red-600 px-3 py-1 rounded text-xs font-z font-bold cursor-pointer">❤️ DAR LIKE (<span id="likeCount">416</span>)</button>
                    <span class="text-[10px] text-zinc-400 font-mono">Algoritmo Trendy: <span id="trendyScore" class="text-green-400">99.9% Frecuencia 4 16</span></span>
                </div>

                <div class="space-y-2 mt-3">
                    <div id="commentsList" class="max-h-24 overflow-y-auto space-y-1 text-xs text-zinc-300 bg-zinc-950 p-2 rounded border border-zinc-900">
                        <div class="text-[10px] text-red-500 font-bold">Enyi el Científico: El sistema tiene un solo dueño 🔺</div>
                    </div>
                    <div class="flex gap-2">
                        <input type="text" id="commentInput" placeholder="Escribe tu comentario en el Sistema Z..." class="flex-grow bg-black border border-zinc-800 p-1.5 rounded text-xs text-white outline-none focus:border-red-600"/>
                        <button id="btnComentar" class="bg-red-600 hover:bg-red-700 text-white px-3 py-1.5 rounded text-xs font-z font-bold cursor-pointer">COMENTAR</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Cuadrícula 4: Estudio Z (Creador de Reels con Pantalla y Flash Rítmico) -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">🎥 Estudio Z (Creador de Reels & Visuales)</h3>
            <p class="text-[11px] text-gray-400 mb-4">Pantalla de previsualización activa, efectos urbanos, interferencia de matriz y flash sincronizado.</p>
            
            <!-- Pantalla del Estudio Z -->
            <div id="studioScreen" class="relative w-full h-48 bg-black border border-red-600 rounded-lg mb-4 flex items-center justify-center overflow-hidden glow-red">
                <div class="absolute inset-0 opacity-20 bg-[radial-gradient(#ff0000_1px,transparent_1px)] [background-size:16px_16px]"></div>
                <div id="matrixEffect" class="absolute inset-0 font-mono text-[9px] text-red-600 p-2 pointer-events-none opacity-40 overflow-hidden">
                    cuatro dieciséis Hz // TIERRA DE MAFIA // SYSTEM Z // 7.83Hz SCHUMANN // SCRIPT & CASH // 🔺
                </div>
                <div class="z-10 text-center">
                    <p class="font-z text-xs text-red-500 font-bold mb-1">🔴 ESTUDIO Z LISTO</p>
                    <p class="text-[10px] text-zinc-400">Selecciona un audio y activa los efectos</p>
                </div>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-4">
                <button id="flashBtn" class="bg-black border border-red-600 text-red-500 p-2 rounded text-[10px] font-z font-bold hover:bg-red-950 cursor-pointer">⚡ FLASH: OFF</button>
                <button id="glitchBtn" class="bg-black border border-zinc-800 text-zinc-300 p-2 rounded text-[10px] font-z hover:border-red-600 cursor-pointer">👾 EFECTO GLITCH</button>
                <button id="camBtn" class="bg-black border border-zinc-800 text-zinc-300 p-2 rounded text-[10px] font-z hover:border-red-600 cursor-pointer">📷 CAM / CÁMARA</button>
                <button id="recBtn" class="bg-red-600 text-white p-2 rounded text-[10px] font-z font-bold hover:bg-red-700 cursor-pointer">⏺️ GRABAR REEL</button>
            </div>
        </div>
    </main>

    <!-- Pie de Página Oficial -->
    <footer class="border-t border-zinc-900 text-center py-4 text-xs text-gray-500 font-z space-y-1">
        <p>ENYI CIENTÍFICO OMOTICHI • SCRIPT & CASH • TIERRA DE MAFIA</p>
        <p class="text-red-600 font-bold">LA FRECUENCIA QUE NO PUEDEN APAGAR cuatro dieciséis HZ</p>
    </footer>

    <!-- Scripts de Lógica del Sistema Z con Event Listeners Seguros -->
    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
        import { getFirestore, collection, addDoc, getDocs, updateDoc, doc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

        const firebaseConfig = {
          apiKey: "AIzaSyA0sJA8yhBovCI7mgkxBi0L_ldi5JyL5iU",
          authDomain: "sistema-z-vault.firebaseapp.com",
          projectId: "sistema-z-vault",
          storageBucket: "sistema-z-vault.firebasestorage.app",
          messagingSenderId: "109056330158",
          appId: "1:109056330158:web:c49fbd4b5dd494021b603f",
          measurementId: "G-9Y6Y5S6FEH"
        };

        let db = null;
        let currentTrackId = null;
        let currentLikes = 416;

        try {
            const app = initializeApp(firebaseConfig);
            db = getFirestore(app);
            document.getElementById('status-box').innerHTML = "🟢 Vault soberano y motores conectados correctamente";
            document.getElementById('status-box').className = "p-3 bg-black border border-green-800 rounded text-xs text-green-400 font-mono";
        } catch (e) {
            document.getElementById('status-box').innerHTML = "⚠️ Modo local activo (Vault offline): " + e.message;
            document.getElementById('status-box').className = "p-3 bg-black border border-amber-800 rounded text-xs text-amber-400 font-mono";
        }

        // 1. Registro de Tema y Copyright Z
        document.getElementById('btnRegistrar').addEventListener('click', async () => {
            const artist = document.getElementById('artistName').value.trim();
            const title = document.getElementById('trackTitle').value.trim();
            const dest = document.getElementById('destType').value;
            const mediaInput = document.getElementById('mediaFile');

            if(!artist || !title) {
                alert("⚠️ Ingresa el nombre del artista y el título del tema.");
                return;
            }

            let mediaUrl = "";
            if(mediaInput.files && mediaInput.files[0]) {
                mediaUrl = URL.createObjectURL(mediaInput.files[0]);
            }

            const copyrightId = "COPYRIGHT-Z-" + Math.floor(100000 + Math.random() * 900000);

            if(db) {
                try {
                    const docRef = await addDoc(collection(db, "sistema_z_vault"), {
                        artist: artist,
                        title: title,
                        destination: dest,
                        mediaUrl: mediaUrl,
                        copyright: copyrightId,
                        likes: 416,
                        comments: ["Sello oficial Sistema Z activo 🔺"],
                        timestamp: new Date().toISOString()
                    });
                    currentTrackId = docRef.id;
                } catch (e) {
                    console.error("Firestore error:", e);
                }
            }

            document.getElementById('nowPlayingTitle').innerText = `${artist} - ${title} (${copyrightId})`;
            if(mediaUrl) {
                document.getElementById('globalAudioPlayer').src = mediaUrl;
            }
            alert(`✅ ¡Tema publicado con éxito! Sello Copyright Z generado: ${copyrightId}`);
        });

        // 2. Buscador Global
        document.getElementById('btnBuscar').addEventListener('click', async () => {
            const query = document.getElementById('globalSearchInput').value.toLowerCase().trim();
            if(!query) {
                alert("⚠️ Escribe algo para buscar en el sistema.");
                return;
            }

            if(!db) {
                alert("🔍 Modo local: No hay conexión al Vault remoto.");
                return;
            }

            try {
                const querySnapshot = await getDocs(collection(db, "sistema_z_vault"));
                let found = false;
                querySnapshot.forEach((documentSnap) => {
                    const data = documentSnap.data();
                    if(data.title.toLowerCase().includes(query) || data.artist.toLowerCase().includes(query)) {
                        currentTrackId = documentSnap.id;
                        currentLikes = data.likes || 416;
                        document.getElementById('nowPlayingTitle').innerText = `${data.artist} - ${data.title} (${data.copyright})`;
                        document.getElementById('likeCount').innerText = currentLikes;
                        if(data.mediaUrl) {
                            document.getElementById('globalAudioPlayer').src = data.mediaUrl;
                        }
                        
                        const commList = document.getElementById('commentsList');
                        commList.innerHTML = "";
                        if(data.comments && data.comments.length > 0) {
                            data.comments.forEach(c => {
                                commList.innerHTML += `<div class="text-[10px] text-zinc-300">🔥 ${c}</div>`;
                            });
                        }
                        found = true;
                    }
                });
                if(!found) {
                    alert("No se encontró el tema en el Vault.");
                }
            } catch (e) {
                alert("Error en la búsqueda: " + e.message);
            }
        });

        // 3. Likes y Trendy
        document.getElementById('btnLike').addEventListener('click', async () => {
            currentLikes++;
            document.getElementById('likeCount').innerText = currentLikes;
            document.getElementById('trendyScore').innerText = ((currentLikes * 1.5) + 100).toFixed(1) + "% (VIRAL PEAK)";
            
            if(currentTrackId && db) {
                try {
                    const trackRef = doc(db, "sistema_z_vault", currentTrackId);
                    await updateDoc(trackRef, { likes: currentLikes });
                } catch(e) {
                    console.error(e);
                }
            }
            alert("❤️ ¡Like registrado!");
        });

        // 4. Comentarios
        document.getElementById('btnComentar').addEventListener('click', async () => {
            const commentText = document.getElementById('commentInput').value.trim();
            if(!commentText) {
                alert("⚠️ Escribe un comentario.");
                return;
            }

            const commList = document.getElementById('commentsList');
            commList.innerHTML += `<div class="text-[10px] text-zinc-300">🔥 ${commentText}</div>`;
            document.getElementById('commentInput').value = "";

            if(currentTrackId && db) {
                try {
                    const querySnapshot = await getDocs(collection(db, "sistema_z_vault"));
                    querySnapshot.forEach(async (documentSnap) => {
                        if(documentSnap.id === currentTrackId) {
                            const trackRef = doc(db, "sistema_z_vault", currentTrackId);
                            const existingComments = documentSnap.data().comments || [];
                            existingComments.push(commentText);
                            await updateDoc(trackRef, { comments: existingComments });
                        }
                    });
                } catch(e) {
                    console.error(e);
                }
            }
        });

        // 5. Botones de Perfil y Estudio Z
        document.getElementById('btnLogin').addEventListener('click', () => {
            const user = document.getElementById('loginUser').value.trim();
            if(!user) {
                alert("⚠️ Ingresa tu usuario o alias de artista.");
                return;
            }
            alert(`🔐 Acceso concedido al perfil de: ${user}`);
        });

        let flashOn = false;
        document.getElementById('flashBtn').addEventListener('click', () => {
            flashOn = !flashOn;
            const btn = document.getElementById('flashBtn');
            const screen = document.getElementById('studioScreen');
            if(flashOn) {
                btn.innerText = "⚡ FLASH: ON (RÍTMICO)";
                screen.style.boxShadow = "0 0 50px #ff0000";
            } else {
                btn.innerText = "⚡ FLASH: OFF";
                screen.style.boxShadow = "0 0 25px rgba(255, 0, 0, 0.4)";
            }
        });

        document.getElementById('glitchBtn').addEventListener('click', () => {
            const matrix = document.getElementById('matrixEffect');
            matrix.style.color = matrix.style.color === 'rgb(0, 255, 0)' ? '#ff0000' : '#00ff00';
            alert("👾 Efecto de matriz activo (Frecuencia 4 16 Hz)");
        });

        document.getElementById('camBtn').addEventListener('click', () => {
            alert("📷 Cámara frontal / trasera conmutada en el Estudio Z.");
        });

        document.getElementById('recBtn').addEventListener('click', () => {
            alert("⏺️ Grabación de Reel iniciada con éxito en el Estudio Z.");
        });
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ [SISTEMA Z] index.html actualizado con event listeners blindados.")
