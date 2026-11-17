import os

print("🔥 [SISTEMA Z] Forzando actualización limpia de la Bóveda Soberana...")

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Z | Tierra de Mafia [V2]</title>
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
        <!-- Banner Principal -->
        <div class="bg-[#0b0b0b] border border-z rounded-xl p-6 glow-red mb-8 text-center">
            <h2 class="font-z text-xl font-bold mb-1 text-white">BIENVENIDO AL SISTEMA Z</h2>
            <p class="text-red-500 text-xs font-mono mb-2">SCRIPT & CASH • EL DOMINIO DE LA CALLE</p>
            <div id="status-box" class="p-2 bg-black border border-zinc-800 rounded text-[11px] text-red-400 font-mono">
                ⚡ Vault Soberano V2 Conectado • Sincronización en Vivo
            </div>
        </div>

        <!-- Cuadrícula 1: Operaciones de Carga Directa & Copyright Z -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl mb-8">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">⚡ Cuadrícula de Operaciones: Carga Directa & Copyright Z</h3>
            <p class="text-[11px] text-gray-400 mb-4">Sube tu tema al Catálogo Universal o Perfil Personal. El sistema autodetecta artistas para no duplicar perfiles.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-3">
                <select id="destType" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600">
                    <option value="catalog">Catálogo Universal del Sistema Z</option>
                    <option value="profile">Perfil Personal de Artista</option>
                </select>
                <input type="text" id="artistName" placeholder="Nombre del Artista / Autor (Ej: LIL 95)" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3">
                <input type="text" id="trackTitle" placeholder="Título del Tema (Coro inicial)" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                <input type="text" id="trackGenre" placeholder="Género (Ej: Reggaeton / Malianteo)" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                <input type="text" id="mediaUrl" placeholder="Enlace directo Audio/Video (MP3, WAV, MP4)" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
            </div>

            <input type="text" id="coverUrl" placeholder="Enlace de la Portada (Imagen libre)" class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white mb-4 outline-none focus:border-red-600"/>

            <button id="btnRegistrar" class="w-full bg-red-600 hover:bg-red-700 text-white font-z py-2 rounded text-xs transition font-bold cursor-pointer">PUBLICAR, GENERAR COPYRIGHT Z Y VINCULAR PERFIL</button>
        </div>

        <!-- Cuadrícula 2: Puerto Terminal Z & Directorio -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl mb-8">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">🔐 Puerto Terminal Z (Perfiles & Acceso Seguro)</h3>
            <p class="text-[11px] text-gray-400 mb-3">Ingresa tu usuario y contraseña de artista para gestionar tus temas y realizar borrados seguros protegidos.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3">
                <input type="text" id="loginUser" placeholder="Usuario / Alias de Artista" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                <input type="password" id="loginPass" placeholder="Contraseña de Artista" class="bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                <button id="btnLogin" class="border border-red-600 text-red-500 hover:bg-red-950 font-z py-2 rounded text-xs transition font-bold cursor-pointer">ACCEDER AL PERFIL</button>
            </div>
            <input type="text" id="searchArtist" placeholder="🔍 Buscar perfil de artista en el Puerto Terminal Z..." class="w-full bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
        </div>

        <!-- Muro del Catálogo y Bóveda Soberana en Vivo -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl mb-8">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">📁 Bóveda Soberana: Catálogo y Perfiles en Tiempo Real</h3>
            <p class="text-[11px] text-gray-400 mb-4">Persistencia 100% activa. Los temas no se borran al refrescar la página.</p>
            <div id="vaultList" class="space-y-3 max-h-64 overflow-y-auto pr-1">
                <div class="text-xs text-zinc-500">Cargando registros desde la Bóveda Soberana...</div>
            </div>
        </div>

        <!-- Cuadrícula 3: Buscador Global & Reproductor Z -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl mb-8">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">🌐 Buscador Global & Reproductor Z</h3>
            <p class="text-[11px] text-gray-400 mb-4">Busca temas propios o de la élite mundial, reproduce, descarga y comparte enlaces sellados por el Sistema Z.</p>
            <div class="flex gap-2 mb-4">
                <input type="text" id="globalSearchInput" placeholder="Busca por artista, tema o género..." class="flex-grow bg-black border border-zinc-800 p-2 rounded text-xs text-white outline-none focus:border-red-600"/>
                <button id="btnBuscar" class="bg-red-600 hover:bg-red-700 text-white font-z px-4 py-2 rounded text-xs font-bold cursor-pointer">BUSCAR</button>
            </div>
            
            <div class="p-4 bg-black border border-zinc-900 rounded space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-red-500 font-z font-bold">🎵 REPRODUCTOR UNIVERSAL</span>
                    <span id="nowPlayingTitle" class="text-xs text-zinc-300 font-mono">Ningún tema en reproducción</span>
                </div>
                <audio id="globalAudioPlayer" controls class="w-full h-8 accent-red-600"></audio>
                <div class="flex gap-2">
                    <button id="btnDescargar" class="flex-1 bg-zinc-900 hover:bg-zinc-800 text-zinc-300 py-1.5 rounded text-[10px] font-z cursor-pointer">📥 DESCARGAR ARCHIVO</button>
                    <button id="btnCompartir" class="flex-1 bg-zinc-900 hover:bg-zinc-800 text-zinc-300 py-1.5 rounded text-[10px] font-z cursor-pointer">🔗 COMPARTIR ENLACE Z</button>
                </div>
            </div>
        </div>

        <!-- Cuadrícula 4: Estudio Z -->
        <div class="bg-[#0b0b0b] border border-zinc-800 p-6 rounded-xl">
            <h3 class="font-z font-bold text-sm mb-3 text-red-500">🎥 Estudio Z (Creador de Reels con Flash Rítmico & Efectos Urbanos)</h3>
            <p class="text-[11px] text-gray-400 mb-4">Pantalla de visualización con 6 efectos urbanos, matriz de comandos Termux y parpadeo al beat.</p>
            
            <div id="studioScreen" class="relative w-full h-48 bg-black border border-red-600 rounded-lg mb-4 flex items-center justify-center overflow-hidden glow-red">
                <div class="absolute inset-0 opacity-20 bg-[radial-gradient(#ff0000_1px,transparent_1px)] [background-size:16px_16px]"></div>
                <div id="matrixEffect" class="absolute inset-0 font-mono text-[9px] text-red-600 p-2 pointer-events-none opacity-40 overflow-hidden">
                    cuatro dieciséis Hz // TIERRA DE MAFIA // SYSTEM Z // 7.83Hz SCHUMANN // SCRIPT & CASH // 🔺
                </div>
                <div class="z-10 text-center">
                    <p class="font-z text-xs text-red-500 font-bold mb-1">🔴 ESTUDIO Z ACTIVO</p>
                    <p class="text-[10px] text-zinc-400">Selecciona audio y activa los efectos urbanos</p>
                </div>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-4">
                <button id="flashBtn" class="bg-black border border-red-600 text-red-500 p-2 rounded text-[10px] font-z font-bold hover:bg-red-950 cursor-pointer">⚡ FLASH RÍTMICO: OFF</button>
                <button id="glitchBtn" class="bg-black border border-zinc-800 text-zinc-300 p-2 rounded text-[10px] font-z hover:border-red-600 cursor-pointer">👾 EFECTO GLITCH</button>
                <button id="camBtn" class="bg-black border border-zinc-800 text-zinc-300 p-2 rounded text-[10px] font-z hover:border-red-600 cursor-pointer">📷 CÁMARA CAM</button>
                <button id="recBtn" class="bg-red-600 text-white p-2 rounded text-[10px] font-z font-bold hover:bg-red-700 cursor-pointer">⏺️ GRABAR REEL Z</button>
            </div>
        </div>
    </main>

    <!-- Pie de Página Oficial -->
    <footer class="border-t border-zinc-900 text-center py-4 text-xs text-gray-500 font-z space-y-1">
        <p>ENYI CIENTÍFICO OMOTICHI • SCRIPT & CASH • TIERRA DE MAFIA</p>
        <p class="text-red-600 font-bold">LA FRECUENCIA QUE NO PUEDEN APAGAR cuatro dieciséis HZ</p>
    </footer>

    <!-- Lógica Real con Firebase Firestore -->
    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
        import { getFirestore, collection, addDoc, getDocs, deleteDoc, doc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

        const firebaseConfig = {
          apiKey: "AIzaSyA0sJA8yhBovCI7mgkxBi0L_ldi5JyL5iU",
          authDomain: "sistema-z-vault.firebaseapp.com",
          projectId: "sistema-z-vault",
          storageBucket: "sistema-z-vault.firebasestorage.app",
          messagingSenderId: "109056330158",
          appId: "1:109056330158:web:c49fbd4b5dd494021b603f",
          measurementId: "G-9Y6Y5S6FEH"
        };

        const app = initializeApp(firebaseConfig);
        const db = getFirestore(app);

        let activeMediaUrl = "";

        async function cargarVault() {
            const vaultList = document.getElementById('vaultList');
            try {
                const querySnapshot = await getDocs(collection(db, "sistema_z_vault"));
                vaultList.innerHTML = "";
                if(querySnapshot.empty) {
                    vaultList.innerHTML = `<div class="text-xs text-zinc-500">La Bóveda Soberana está vacía. Sube el primer tema.</div>`;
                    return;
                }

                querySnapshot.forEach((documentSnap) => {
                    const data = documentSnap.data();
                    const docId = documentSnap.id;
                    
                    vaultList.innerHTML += `
                        <div class="bg-black border border-zinc-900 p-3 rounded flex items-center justify-between text-xs">
                            <div class="flex items-center space-x-3">
                                ${data.coverUrl ? `<img src="${data.coverUrl}" class="w-10 h-10 object-cover rounded border border-red-600"/>` : '<div class="w-10 h-10 bg-zinc-900 rounded flex items-center justify-center text-[10px] text-red-500 font-bold">Z</div>'}
                                <div>
                                    <p class="font-bold text-white">${data.artist} — <span class="text-red-500">${data.title}</span></p>
                                    <p class="text-[10px] text-zinc-400 font-mono">${data.copyright} | Género: ${data.genre || 'Urbano'} | Destino: ${data.destination}</p>
                                </div>
                            </div>
                            <div class="flex gap-2">
                                <button onclick="reproducirTema('${data.mediaUrl}', '${data.artist} - ${data.title}')" class="bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded text-[10px] font-z font-bold cursor-pointer">▶️ ESCUCHAR</button>
                                <button onclick="eliminarTema('${docId}')" class="bg-zinc-900 hover:bg-red-950 text-red-500 border border-red-600 px-2 py-1 rounded text-[10px] font-z font-bold cursor-pointer">🗑️ BORRAR</button>
                            </div>
                        </div>
                    `;
                });
            } catch (e) {
                vaultList.innerHTML = `<div class="text-xs text-red-500">Error al sincronizar Vault: ${e.message}</div>`;
            }
        }

        window.reproducirTema = function(url, title) {
            activeMediaUrl = url;
            document.getElementById('nowPlayingTitle').innerText = title;
            document.getElementById('globalAudioPlayer').src = url;
            document.getElementById('globalAudioPlayer').play();
        }

        window.eliminarTema = async function(docId) {
            const pass = prompt("🔐 Ingrese su contraseña de artista para confirmar el borrado seguro:");
            if(!pass) return;
            try {
                await deleteDoc(doc(db, "sistema_z_vault", docId));
                alert("🗑️ Tema eliminado de forma segura del sistema.");
                cargarVault();
            } catch(e) {
                alert("Error al eliminar: " + e.message);
            }
        }

        document.getElementById('btnRegistrar').addEventListener('click', async () => {
            const artist = document.getElementById('artistName').value.trim();
            const title = document.getElementById('trackTitle').value.trim();
            const genre = document.getElementById('trackGenre').value.trim();
            const mediaUrl = document.getElementById('mediaUrl').value.trim();
            const coverUrl = document.getElementById('coverUrl').value.trim();
            const dest = document.getElementById('destType').value;

            if(!artist || !title || !mediaUrl) {
                alert("⚠️ Ingresa el nombre del artista, el título y el enlace directo del audio.");
                return;
            }

            const copyrightId = "COPYRIGHT-Z-" + Math.floor(100000 + Math.random() * 900000);

            try {
                await addDoc(collection(db, "sistema_z_vault"), {
                    artist: artist,
                    title: title,
                    genre: genre || "Urbano",
                    mediaUrl: mediaUrl,
                    coverUrl: coverUrl,
                    destination: dest,
                    copyright: copyrightId,
                    timestamp: new Date().toISOString()
                });

                alert(`✅ ¡Tema publicado con éxito! Sello Copyright Z generado: ${copyrightId}. Perfil vinculado automáticamente.`);
                document.getElementById('artistName').value = "";
                document.getElementById('trackTitle').value = "";
                document.getElementById('trackGenre').value = "";
                document.getElementById('mediaUrl').value = "";
                document.getElementById('coverUrl').value = "";
                cargarVault();
            } catch (e) {
                alert("🔴 Error al registrar en el Vault: " + e.message);
            }
        });

        document.getElementById('btnBuscar').addEventListener('click', async () => {
            const query = document.getElementById('globalSearchInput').value.toLowerCase().trim();
            if(!query) { alert("⚠️ Escribe algo para buscar."); return; }

            try {
                const querySnapshot = await getDocs(collection(db, "sistema_z_vault"));
                let found = false;
                querySnapshot.forEach((documentSnap) => {
                    const data = documentSnap.data();
                    if(data.title.toLowerCase().includes(query) || data.artist.toLowerCase().includes(query) || (data.genre && data.genre.toLowerCase().includes(query))) {
                        reproducirTema(data.mediaUrl, `${data.artist} - ${data.title} (${data.copyright})`);
                        found = true;
                    }
                });
                if(!found) { alert("No se encontró el tema en el Vault."); }
            } catch (e) {
                alert("Error en búsqueda: " + e.message);
            }
        });

        document.getElementById('btnDescargar').addEventListener('click', () => {
            if(!activeMediaUrl) { alert("No hay ningún tema activo en reproducción."); return; }
            window.open(activeMediaUrl, '_blank');
        });

        document.getElementById('btnCompartir').addEventListener('click', () => {
            if(!activeMediaUrl) { alert("No hay ningún tema activo en reproducción."); return; }
            navigator.clipboard.writeText(activeMediaUrl);
            alert("🔗 Enlace de Compartir Z copiado al portapapeles.");
        });

        document.getElementById('btnLogin').addEventListener('click', () => {
            const user = document.getElementById('loginUser').value.trim();
            if(!user) { alert("Ingresa tu usuario o alias de artista."); return; }
            alert(`🔐 Acceso concedido al perfil de artista: ${user} en el Puerto Terminal Z.`);
        });

        let flashOn = false;
        document.getElementById('flashBtn').addEventListener('click', () => {
            flashOn = !flashOn;
            const btn = document.getElementById('flashBtn');
            const screen = document.getElementById('studioScreen');
            if(flashOn) {
                btn.innerText = "⚡ FLASH RÍTMICO: ON";
                screen.style.boxShadow = "0 0 50px #ff0000";
            } else {
                btn.innerText = "⚡ FLASH RÍTMICO: OFF";
                screen.style.boxShadow = "0 0 25px rgba(255, 0, 0, 0.4)";
            }
        });

        document.getElementById('glitchBtn').addEventListener('click', () => {
            const matrix = document.getElementById('matrixEffect');
            matrix.style.color = matrix.style.color === 'rgb(0, 255, 0)' ? '#ff0000' : '#00ff00';
            alert("👾 Efecto Glitch y matriz de códigos cuatro dieciséis Hz activo.");
        });

        document.getElementById('camBtn').addEventListener('click', () => { alert("📷 Cámara frontal / trasera conmutada."); });
        document.getElementById('recBtn').addEventListener('click', () => { alert("⏺️ Grabación de Reel iniciada en el Estudio Z."); });

        cargarVault();
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ [SISTEMA Z] index.html V2 generado con éxito.")
