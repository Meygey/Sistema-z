/**
 * 🔺 SISTEMA Z - ESTUDIO DE GRABACIÓN DE REELS (MÓDULO INDEPENDIENTE)
 * Cámara en vivo, audio del catálogo con recorte, mezcla Web Audio, 7 efectos visuales urbanos, descarga y compartir.
 */
window.EstudioReelsZ = {
    stream: null,
    recordStream: null,
    canvasStream: null,
    mediaRecorder: null,
    chunks: [],
    facingMode: "user", // 'user' = frontal, 'environment' = trasera
    torchOn: false,
    beatFlashActivo: false,
    temasCatalogo: [],
    audioEl: null,
    audioCtx: null,
    audioSource: null,
    analyser: null,
    audioDest: null,
    renderRafId: null,
    lastTorchPulse: 0,
    matrixCols: [],
    smokePuffs: [],
    cmdLines: [],

    efectos: {
        matriz: false,
        distorsion: false,
        comandos: false,
        pulsacion: true,
        aura: false,
        camaraLenta: false,
        humo: false
    },

    abrirEstudio: function() {
        if (document.getElementById('z-reel-modal')) {
            document.getElementById('z-reel-modal').style.display = 'flex';
            this.cargarTemasParaReel();
            this.iniciarCamara();
            return;
        }

        const modal = document.createElement('div');
        modal.id = 'z-reel-modal';
        modal.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(5, 5, 5, 0.97); z-index: 100000;
            display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
            font-family: monospace; color: #fff; padding: 10px; box-sizing: border-box; overflow-y: auto;
        `;

        modal.innerHTML = `
            <div style="width: 100%; max-width: 410px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="color: #ff1a1a; font-weight: bold;">🎥 ESTUDIO REELS 416Hz</span>
                <button id="z-cerrar-estudio" style="background: #222; color: #fff; border: 1px solid #ff1a1a; padding: 4px 10px; border-radius: 4px; cursor: pointer;">✕ Cerrar</button>
            </div>

            <div style="width: 100%; max-width: 410px; background: #111; border: 1px solid #333; border-radius: 8px; padding: 7px; margin-bottom: 6px; font-size: 11px;">
                <label style="display:block; color:#aaa; margin-bottom:3px;">🎵 Tema del catálogo (mezcla directa)</label>
                <select id="z-reel-track-select" style="width:100%; padding:5px; background:#000; color:#fff; border:1px solid #444; border-radius:4px; margin-bottom:5px;">
                    <option value="">-- Solo cámara / micrófono --</option>
                </select>
                <div style="display:flex; gap:8px; align-items:center; justify-content:space-between;">
                    <label style="color:#aaa;">✂️ Inicio (seg):
                        <input id="z-reel-start-sec" type="number" min="0" max="600" value="0" style="width:58px; padding:3px; background:#000; color:#fff; border:1px solid #444; border-radius:4px;" />
                    </label>
                    <button id="z-btn-preview-audio" style="background:#1a1a1a; color:#00ff88; border:1px solid #00ff88; padding:4px 9px; border-radius:4px; cursor:pointer; font-weight:bold;">▶ Probar Tramo</button>
                </div>
            </div>

            <div style="position: relative; width: 100%; max-width: 340px; aspect-ratio: 9/16; background: #000; border: 2px solid #ff1a1a; border-radius: 10px; overflow: hidden;">
                <video id="z-reel-preview" autoplay playsinline muted style="display:none;"></video>
                <canvas id="z-reel-canvas" width="540" height="960" style="width: 100%; height: 100%; object-fit: cover; display: block;"></canvas>
                <div id="z-rec-indicator" style="display: none; position: absolute; top: 10px; left: 10px; background: #ff1a1a; color: #fff; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">● REC</div>
            </div>

            <div style="width: 100%; max-width: 410px; background: #101010; border: 1px solid #2b2b2b; border-radius: 8px; padding: 6px; margin-top: 6px;">
                <div style="font-size: 11px; color: #ff4d4d; font-weight: bold; margin-bottom: 5px;">🎛️ EFECTOS URBANOS SISTEMA Z (TOCA PARA ACTIVAR)</div>
                <div id="z-fx-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 5px; font-size: 11px;">
                    <button data-fx="matriz" class="z-fx-btn" style="padding:6px; border-radius:5px; border:1px solid #333; background:#191919; color:#ddd; cursor:pointer;">🟩 Fallo Matriz</button>
                    <button data-fx="distorsion" class="z-fx-btn" style="padding:6px; border-radius:5px; border:1px solid #333; background:#191919; color:#ddd; cursor:pointer;">📺 Distorsión / Interferencia</button>
                    <button data-fx="comandos" class="z-fx-btn" style="padding:6px; border-radius:5px; border:1px solid #333; background:#191919; color:#ddd; cursor:pointer;">⌨️ Códigos Comandos</button>
                    <button data-fx="pulsacion" class="z-fx-btn" style="padding:6px; border-radius:5px; border:1px solid #ff1a1a; background:#4a0a0a; color:#fff; cursor:pointer;">💓 Pulsación al Beat</button>
                    <button data-fx="aura" class="z-fx-btn" style="padding:6px; border-radius:5px; border:1px solid #333; background:#191919; color:#ddd; cursor:pointer;">✨ Aura y Estela</button>
                    <button data-fx="camaraLenta" class="z-fx-btn" style="padding:6px; border-radius:5px; border:1px solid #333; background:#191919; color:#ddd; cursor:pointer;">🐢 Cámara Lenta</button>
                    <button data-fx="humo" class="z-fx-btn" style="grid-column: span 2; padding:6px; border-radius:5px; border:1px solid #333; background:#191919; color:#ddd; cursor:pointer;">💨 Humo Intenso Urbano</button>
                </div>
            </div>

            <div style="width: 100%; max-width: 410px; display: flex; flex-wrap: wrap; justify-content: space-around; align-items: center; margin-top: 8px; gap: 6px;">
                <button id="z-btn-cam-flip" style="background: #1a1a1a; color: #fff; border: 1px solid #444; padding: 7px 9px; border-radius: 6px; cursor: pointer; font-size:12px;">🔄 Cámara</button>
                <button id="z-btn-rec" style="background: #ff1a1a; color: #fff; border: none; padding: 9px 16px; border-radius: 50px; font-weight: bold; cursor: pointer; font-size:12px;">● GRABAR</button>
                <button id="z-btn-torch" style="background: #1a1a1a; color: #fff; border: 1px solid #444; padding: 7px 9px; border-radius: 6px; cursor: pointer; font-size:12px;">🔦 Flash</button>
                <button id="z-btn-beat-flash" style="background: #1a1a1a; color: #ffd700; border: 1px solid #665500; padding: 7px 9px; border-radius: 6px; cursor: pointer; font-size:12px;">⚡ Flash Beat</button>
            </div>

            <div id="z-reel-resultado" style="margin-top: 8px; text-align: center; width: 100%; max-width: 410px;"></div>
        `;

        document.body.appendChild(modal);
        this.inicializarParticulasEfectos();

        document.getElementById('z-cerrar-estudio').onclick = () => this.cerrarEstudio();
        document.getElementById('z-btn-cam-flip').onclick = () => this.cambiarCamara();
        document.getElementById('z-btn-torch').onclick = () => this.alternarFlash();
        document.getElementById('z-btn-beat-flash').onclick = () => this.alternarBeatFlash();
        document.getElementById('z-btn-rec').onclick = () => this.alternarGrabacion();
        document.getElementById('z-btn-preview-audio').onclick = () => this.reproducirTramoSeleccionado();

        modal.querySelectorAll('.z-fx-btn').forEach(btn => {
            btn.onclick = () => {
                const key = btn.getAttribute('data-fx');
                if (!key) return;
                this.efectos[key] = !this.efectos[key];
                const activo = this.efectos[key];
                btn.style.border = activo ? "1px solid #ff1a1a" : "1px solid #333";
                btn.style.background = activo ? "#4a0a0a" : "#191919";
                btn.style.color = activo ? "#fff" : "#ddd";
                if (activo) {
                    this.prepararMezclaAudio(document.getElementById('z-reel-track-select')?.value || "");
                }
            };
        });

        this.cargarTemasParaReel();
        this.iniciarCamara();
        this.iniciarRenderLoop();
    },

    inicializarParticulasEfectos: function() {
        const colsCount = 27;
        this.matrixCols = Array.from({ length: colsCount }, (_, i) => ({
            x: i * 20,
            y: Math.random() * 960,
            speed: 4 + Math.random() * 8,
            dir: i % 2 === 0 ? 1 : -1
        }));

        this.smokePuffs = Array.from({ length: 22 }, () => ({
            x: Math.random() * 540,
            y: 520 + Math.random() * 440,
            r: 55 + Math.random() * 95,
            vx: (Math.random() - 0.5) * 1.4,
            vy: -0.6 - Math.random() * 1.3,
            alpha: 0.14 + Math.random() * 0.18
        }));

        const cmds = [
            "> SYS.Z // 416HZ_LOCKED",
            "> SCHUMANN_RESONANCE: 7.83HZ",
            "> TRIADA_PROTOCOL: ACTIVE",
            "> AUDIO_BUS: MIX_STUDIO_Z",
            "> MALIANTEO_CORE: READY",
            "> SCAN_FREQ: -97.26_CENTS"
        ];
        this.cmdLines = Array.from({ length: 12 }, (_, idx) => ({
            text: cmds[idx % cmds.length],
            x: 18 + (idx % 3) * 14,
            y: idx * 80,
            vy: idx % 2 === 0 ? -1.8 : 1.8
        }));
    },

    cargarTemasParaReel: async function() {
        const select = document.getElementById('z-reel-track-select');
        if (!select) return;
        try {
            const urlBase = typeof SUPABASE_URL !== "undefined" ? SUPABASE_URL : "https://uxyvpqraebwptbbvngus.supabase.co";
            const keyBase = typeof SUPABASE_ANON_KEY !== "undefined" ? SUPABASE_ANON_KEY : "";
            const headers = keyBase ? { "apikey": keyBase, "Authorization": `Bearer ${keyBase}` } : {};
            const res = await fetch(`${urlBase}/rest/v1/temas_z?select=*`, { headers });
            if (!res.ok) return;
            const rows = await res.json();
            if (!Array.isArray(rows)) return;
            this.temasCatalogo = rows;

            const currentVal = select.value;
            select.innerHTML = `<option value="">-- Solo cámara / micrófono --</option>`;
            rows.forEach((t, idx) => {
                const audioUrl = t.audio_url || t.url_audio || t.url || t.media_url || "";
                if (!audioUrl) return;
                const titulo = t.titulo || t.nombre || `Tema #${idx + 1}`;
                const artista = t.artista || "";
                const opt = document.createElement('option');
                opt.value = audioUrl;
                opt.textContent = artista ? `${artista} — ${titulo}` : titulo;
                select.appendChild(opt);
            });
            if (currentVal) select.value = currentVal;
        } catch (err) {
            if (window.zLog) zLog("ESTUDIO", "No se pudo cargar catálogo en Reel: " + err.message, "WARN");
        }
    },

    prepararMezclaAudio: function(audioUrl) {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return null;

        if (!this.audioCtx) {
            this.audioCtx = new AudioCtx();
            this.analyser = this.audioCtx.createAnalyser();
            this.analyser.fftSize = 256;
            this.audioDest = this.audioCtx.createMediaStreamDestination();
            this.analyser.connect(this.audioDest);
            this.analyser.connect(this.audioCtx.destination);
        }
        if (this.audioCtx.state === "suspended") {
            this.audioCtx.resume();
        }

        if (this.stream && this.stream.getAudioTracks().length > 0) {
            try {
                const micSrc = this.audioCtx.createMediaStreamSource(this.stream);
                micSrc.connect(this.audioDest);
            } catch (_) {}
        }

        if (audioUrl) {
            if (!this.audioEl) {
                this.audioEl = new Audio();
                this.audioEl.crossOrigin = "anonymous";
            }
            if (this.audioEl.src !== audioUrl) {
                this.audioEl.src = audioUrl;
            }
            if (!this.audioSource) {
                try {
                    this.audioSource = this.audioCtx.createMediaElementSource(this.audioEl);
                    this.audioSource.connect(this.analyser);
                } catch (_) {}
            }
        }
        return this.audioDest ? this.audioDest.stream : null;
    },

    reproducirTramoSeleccionado: function() {
        const select = document.getElementById('z-reel-track-select');
        const startInput = document.getElementById('z-reel-start-sec');
        const audioUrl = select ? select.value : "";
        const inicio = Math.max(0, parseFloat(startInput ? startInput.value : "0") || 0);

        if (!audioUrl) {
            alert("Selecciona primero un tema del catálogo.");
            return;
        }
        this.prepararMezclaAudio(audioUrl);
        if (!this.audioEl) return;

        if (!this.audioEl.paused) {
            this.audioEl.pause();
            return;
        }
        this.audioEl.currentTime = inicio;
        this.audioEl.play().catch(err => alert("No se pudo reproducir el audio: " + err.message));
    },

    obtenerEnergiaBeat: function() {
        if (!this.analyser) return 0;
        const arr = new Uint8Array(this.analyser.frequencyBinCount);
        this.analyser.getByteFrequencyData(arr);
        let sum = 0;
        const bins = Math.min(20, arr.length);
        for (let i = 0; i < bins; i++) sum += arr[i];
        return sum / (bins * 255);
    },

    iniciarRenderLoop: function() {
        if (this.renderRafId) cancelAnimationFrame(this.renderRafId);
        const canvas = document.getElementById('z-reel-canvas');
        const video = document.getElementById('z-reel-preview');
        if (!canvas || !video) return;
        const ctx = canvas.getContext('2d');
        const W = canvas.width;
        const H = canvas.height;
        const glyphs = "01XYZ416⚡▲Ω#%*<>";

        let frameCounter = 0;
        const render = () => {
            frameCounter++;
            const energy = this.obtenerEnergiaBeat();
            const golpe = energy > 0.62;

            // Cámara lenta: salta cuadros alternos o aplica cadencia lenta visual
            if (!this.efectos.camaraLenta || frameCounter % 2 === 0) {
                if (this.efectos.aura) {
                    ctx.fillStyle = "rgba(0, 0, 0, 0.24)";
                    ctx.fillRect(0, 0, W, H);
                } else {
                    ctx.fillStyle = "#000";
                    ctx.fillRect(0, 0, W, H);
                }

                if (video.readyState >= 2) {
                    ctx.save();
                    if (this.efectos.pulsacion && golpe) {
                        const scale = 1.03 + energy * 0.04;
                        ctx.translate(W / 2, H / 2);
                        ctx.scale(scale, scale);
                        ctx.translate(-W / 2, -H / 2);
                    }
                    ctx.globalAlpha = this.efectos.aura ? 0.86 : 1;
                    ctx.drawImage(video, 0, 0, W, H);
                    ctx.restore();
                }
            }

            // 1. Efecto Aura y Estela
            if (this.efectos.aura) {
                const auraGrad = ctx.createRadialGradient(W / 2, H / 2, W * 0.18, W / 2, H / 2, W * 0.72);
                auraGrad.addColorStop(0, "rgba(255, 26, 26, 0)");
                auraGrad.addColorStop(0.7, `rgba(255, 26, 26, ${0.14 + energy * 0.22})`);
                auraGrad.addColorStop(1, `rgba(255, 0, 60, ${0.28 + energy * 0.35})`);
                ctx.fillStyle = auraGrad;
                ctx.fillRect(0, 0, W, H);
            }

            // 2. Pulsación al ritmo del beat
            if (this.efectos.pulsacion && golpe) {
                ctx.strokeStyle = `rgba(255, 26, 26, ${0.35 + energy * 0.45})`;
                ctx.lineWidth = 6 + energy * 10;
                ctx.strokeRect(8, 8, W - 16, H - 16);
                ctx.fillStyle = `rgba(255, 26, 26, ${0.08 + energy * 0.14})`;
                ctx.fillRect(0, 0, W, H);
            }

            // 3. Fallo en la Matriz
            if (this.efectos.matriz) {
                ctx.font = "bold 15px monospace";
                for (const col of this.matrixCols) {
                    const ch = glyphs[Math.floor(Math.random() * glyphs.length)];
                    ctx.fillStyle = Math.random() > 0.82 ? "#ff4d4d" : "#00ff88";
                    ctx.fillText(ch, col.x, col.y);
                    col.y += col.speed * col.dir * (this.efectos.camaraLenta ? 0.5 : 1);
                    if (col.y > H) col.y = 0;
                    if (col.y < 0) col.y = H;
                }
            }

            // 4. Distorsión e Interferencia
            if (this.efectos.distorsion) {
                const slices = golpe ? 9 : 5;
                for (let i = 0; i < slices; i++) {
                    const sy = Math.floor(Math.random() * H);
                    const sh = 10 + Math.floor(Math.random() * 28);
                    const dx = (Math.random() - 0.5) * (golpe ? 44 : 18);
                    ctx.drawImage(canvas, 0, sy, W, sh, dx, sy, W, sh);
                }
                ctx.fillStyle = "rgba(255, 255, 255, 0.04)";
                for (let y = 0; y < H; y += 8) {
                    ctx.fillRect(0, y, W, 2);
                }
            }

            // 5. Códigos de comandos subiendo y bajando
            if (this.efectos.comandos) {
                ctx.font = "bold 13px monospace";
                for (const line of this.cmdLines) {
                    ctx.fillStyle = "rgba(0, 0, 0, 0.55)";
                    ctx.fillRect(line.x - 4, line.y - 14, 240, 20);
                    ctx.fillStyle = line.vy < 0 ? "#00ff88" : "#ff4d4d";
                    ctx.fillText(line.text, line.x, line.y);
                    line.y += line.vy * (this.efectos.camaraLenta ? 0.45 : 1);
                    if (line.y < 20) line.y = H - 20;
                    if (line.y > H - 15) line.y = 25;
                }
            }

            // 6. Humo intenso con toque urbano
            if (this.efectos.humo) {
                for (const p of this.smokePuffs) {
                    const grad = ctx.createRadialGradient(p.x, p.y, 6, p.x, p.y, p.r);
                    grad.addColorStop(0, `rgba(210, 210, 215, ${p.alpha + energy * 0.1})`);
                    grad.addColorStop(0.55, `rgba(90, 20, 25, ${p.alpha * 0.7})`);
                    grad.addColorStop(1, "rgba(0, 0, 0, 0)");
                    ctx.fillStyle = grad;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fill();

                    const slowFactor = this.efectos.camaraLenta ? 0.45 : 1;
                    p.x += p.vx * slowFactor;
                    p.y += p.vy * slowFactor;
                    if (p.y < -p.r) {
                        p.y = H + p.r * 0.5;
                        p.x = Math.random() * W;
                    }
                    if (p.x < -p.r) p.x = W + p.r;
                    if (p.x > W + p.r) p.x = -p.r;
                }
            }

            // 7. Flash físico opcional al ritmo del beat
            if (this.beatFlashActivo && golpe && this.facingMode === "environment" && this.stream) {
                const now = Date.now();
                if (now - this.lastTorchPulse > 340) {
                    this.lastTorchPulse = now;
                    const track = this.stream.getVideoTracks()[0];
                    const cap = track && track.getCapabilities ? track.getCapabilities() : {};
                    if (cap.torch) {
                        track.applyConstraints({ advanced: [{ torch: true }] })
                            .then(() => setTimeout(() => {
                                if (!this.torchOn) track.applyConstraints({ advanced: [{ torch: false }] }).catch(() => {});
                            }, 85))
                            .catch(() => {});
                    }
                }
            }

            this.renderRafId = requestAnimationFrame(render);
        };
        this.renderRafId = requestAnimationFrame(render);
    },

    alternarBeatFlash: function() {
        this.beatFlashActivo = !this.beatFlashActivo;
        const btn = document.getElementById('z-btn-beat-flash');
        if (btn) {
            btn.style.background = this.beatFlashActivo ? "#665500" : "#1a1a1a";
            btn.style.color = this.beatFlashActivo ? "#fff" : "#ffd700";
        }
        if (this.beatFlashActivo) {
            this.prepararMezclaAudio(document.getElementById('z-reel-track-select')?.value || "");
        }
    },

    iniciarCamara: async function() {
        if (this.stream) {
            this.stream.getTracks().forEach(t => t.stop());
        }
        try {
            this.stream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: this.facingMode, width: { ideal: 540 }, height: { ideal: 960 } },
                audio: true
            });
            const video = document.getElementById('z-reel-preview');
            if (video) video.srcObject = this.stream;
            if (window.zLog) zLog("ESTUDIO", "Cámara iniciada en modo: " + this.facingMode, "SUCCESS");
        } catch (err) {
            alert("⚠️ Permite el acceso a cámara y micrófono para usar el Estudio Z: " + err.message);
        }
    },

    cambiarCamara: function() {
        this.facingMode = (this.facingMode === "user") ? "environment" : "user";
        this.torchOn = false;
        this.iniciarCamara();
    },

    alternarFlash: async function() {
        if (!this.stream) return;
        const track = this.stream.getVideoTracks()[0];
        const capabilities = track.getCapabilities ? track.getCapabilities() : {};
        if (!capabilities.torch) {
            alert("⚡ El flash solo está disponible en la cámara trasera de este dispositivo.");
            return;
        }
        this.torchOn = !this.torchOn;
        await track.applyConstraints({ advanced: [{ torch: this.torchOn }] });
    },

    compartirReel: async function(blob) {
        const file = new File([blob], "reel_sistema_z_416.webm", { type: "video/webm" });
        if (navigator.canShare && navigator.canShare({ files: [file] })) {
            try {
                await navigator.share({
                    title: "Reel Sistema Z 416Hz",
                    text: "Grabado en Estudio Reels 416Hz — Sistema Z",
                    files: [file]
                });
                return;
            } catch (err) {
                if (err && err.name === "AbortError") return;
            }
        }
        if (navigator.share) {
            try {
                await navigator.share({
                    title: "Sistema Z 416Hz",
                    text: "Mira lo nuevo en Sistema Z",
                    url: window.location.href
                });
                return;
            } catch (_) {}
        }
        alert("📲 Usa el botón de Descargar Reel para guardar el archivo y compartirlo en tu app favorita.");
    },

    alternarGrabacion: function() {
        const btn = document.getElementById('z-btn-rec');
        const ind = document.getElementById('z-rec-indicator');
        const canvas = document.getElementById('z-reel-canvas');

        if (!this.mediaRecorder || this.mediaRecorder.state === "inactive") {
            if (!this.stream || !canvas) {
                alert("La cámara aún no está lista.");
                return;
            }
            const select = document.getElementById('z-reel-track-select');
            const startInput = document.getElementById('z-reel-start-sec');
            const audioUrl = select ? select.value : "";
            const inicio = Math.max(0, parseFloat(startInput ? startInput.value : "0") || 0);

            const mixedAudioStream = this.prepararMezclaAudio(audioUrl);
            this.canvasStream = canvas.captureStream(30);
            const tracks = [...this.canvasStream.getVideoTracks()];
            if (mixedAudioStream && mixedAudioStream.getAudioTracks().length > 0) {
                tracks.push(mixedAudioStream.getAudioTracks()[0]);
            } else {
                tracks.push(...this.stream.getAudioTracks());
            }
            this.recordStream = new MediaStream(tracks);

            if (audioUrl && this.audioEl) {
                this.audioEl.currentTime = inicio;
                this.audioEl.play().catch(() => {});
            }

            this.chunks = [];
            this.mediaRecorder = new MediaRecorder(this.recordStream);
            this.mediaRecorder.ondataavailable = e => { if (e.data.size > 0) this.chunks.push(e.data); };
            this.mediaRecorder.onstop = () => {
                if (this.audioEl && !this.audioEl.paused) {
                    this.audioEl.pause();
                }
                const blob = new Blob(this.chunks, { type: "video/webm" });
                const url = URL.createObjectURL(blob);
                const resBox = document.getElementById('z-reel-resultado');
                resBox.innerHTML = `
                    <div style="display:flex; gap:10px; justify-content:center; align-items:center; flex-wrap:wrap;">
                        <a href="${url}" download="reel_sistema_z_416.webm" style="color: #00ff88; font-weight: bold; text-decoration: underline;">⬇️ Descargar Reel Grabado</a>
                        <button id="z-btn-compartir-reel" style="background:#1a1a1a; color:#fff; border:1px solid #00ff88; padding:5px 10px; border-radius:6px; cursor:pointer; font-weight:bold;">📤 Compartir</button>
                    </div>
                `;
                const shareBtn = document.getElementById('z-btn-compartir-reel');
                if (shareBtn) {
                    shareBtn.onclick = () => this.compartirReel(blob);
                }
            };
            this.mediaRecorder.start();
            btn.textContent = "⏹ DETENER";
            btn.style.background = "#444";
            ind.style.display = "block";
        } else {
            this.mediaRecorder.stop();
            btn.textContent = "● GRABAR";
            btn.style.background = "#ff1a1a";
            ind.style.display = "none";
        }
    },

    cerrarEstudio: function() {
        if (this.audioEl && !this.audioEl.paused) {
            this.audioEl.pause();
        }
        if (this.renderRafId) {
            cancelAnimationFrame(this.renderRafId);
            this.renderRafId = null;
        }
        if (this.stream) {
            this.stream.getTracks().forEach(t => t.stop());
            this.stream = null;
        }
        const modal = document.getElementById('z-reel-modal');
        if (modal) modal.style.display = 'none';
    }
};
