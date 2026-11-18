/**
 * 🔺 SISTEMA Z - ESTUDIO DE GRABACIÓN DE REELS (MÓDULO INDEPENDIENTE)
 * Cámara en vivo, cambio frontal/trasera, control de linterna/flash y grabación vertical.
 */

window.EstudioReelsZ = {
    stream: null,
    mediaRecorder: null,
    chunks: [],
    facingMode: "user", // 'user' = frontal, 'environment' = trasera
    torchOn: false,

    abrirEstudio: function() {
        if (document.getElementById('z-reel-modal')) {
            document.getElementById('z-reel-modal').style.display = 'flex';
            this.iniciarCamara();
            return;
        }

        const modal = document.createElement('div');
        modal.id = 'z-reel-modal';
        modal.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(5, 5, 5, 0.96); z-index: 100000;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            font-family: monospace; color: #fff; padding: 15px; box-sizing: border-box;
        `;

        modal.innerHTML = `
            <div style="width: 100%; max-width: 400px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="color: #ff1a1a; font-weight: bold;">🎥 ESTUDIO REELS 416Hz</span>
                <button id="z-cerrar-estudio" style="background: #222; color: #fff; border: 1px solid #ff1a1a; padding: 4px 10px; border-radius: 4px; cursor: pointer;">✕ Cerrar</button>
            </div>
            <div style="position: relative; width: 100%; max-width: 400px; aspect-ratio: 9/16; background: #000; border: 2px solid #ff1a1a; border-radius: 10px; overflow: hidden;">
                <video id="z-reel-preview" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover;"></video>
                <div id="z-rec-indicator" style="display: none; position: absolute; top: 12px; left: 12px; background: #ff1a1a; color: #fff; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">● REC</div>
            </div>
            <div style="width: 100%; max-width: 400px; display: flex; justify-content: space-around; align-items: center; margin-top: 15px; gap: 8px;">
                <button id="z-btn-cam-flip" style="background: #1a1a1a; color: #fff; border: 1px solid #444; padding: 10px; border-radius: 6px; cursor: pointer;">🔄 Cámara</button>
                <button id="z-btn-rec" style="background: #ff1a1a; color: #fff; border: none; padding: 12px 20px; border-radius: 50px; font-weight: bold; cursor: pointer;">● GRABAR</button>
                <button id="z-btn-torch" style="background: #1a1a1a; color: #fff; border: 1px solid #444; padding: 10px; border-radius: 6px; cursor: pointer;">⚡ Flash</button>
            </div>
            <div id="z-reel-resultado" style="margin-top: 10px; text-align: center;"></div>
        `;

        document.body.appendChild(modal);

        document.getElementById('z-cerrar-estudio').onclick = () => this.cerrarEstudio();
        document.getElementById('z-btn-cam-flip').onclick = () => this.cambiarCamara();
        document.getElementById('z-btn-torch').onclick = () => this.alternarFlash();
        document.getElementById('z-btn-rec').onclick = () => this.alternarGrabacion();

        this.iniciarCamara();
    },

    iniciarCamara: async function() {
        if (this.stream) {
            this.stream.getTracks().forEach(t => t.stop());
        }
        try {
            this.stream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: this.facingMode },
                audio: true
            });
            document.getElementById('z-reel-preview').srcObject = this.stream;
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

    alternarGrabacion: function() {
        const btn = document.getElementById('z-btn-rec');
        const ind = document.getElementById('z-rec-indicator');

        if (!this.mediaRecorder || this.mediaRecorder.state === "inactive") {
            this.chunks = [];
            this.mediaRecorder = new MediaRecorder(this.stream);
            this.mediaRecorder.ondataavailable = e => { if (e.data.size > 0) this.chunks.push(e.data); };
            this.mediaRecorder.onstop = () => {
                const blob = new Blob(this.chunks, { type: "video/webm" });
                const url = URL.createObjectURL(blob);
                document.getElementById('z-reel-resultado').innerHTML = `
                    <a href="${url}" download="reel_sistema_z_416.webm" style="color: #00ff88; font-weight: bold; text-decoration: underline;">⬇️ Descargar Reel Grabado</a>
                `;
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
        if (this.stream) {
            this.stream.getTracks().forEach(t => t.stop());
            this.stream = null;
        }
        const modal = document.getElementById('z-reel-modal');
        if (modal) modal.style.display = 'none';
    }
};
