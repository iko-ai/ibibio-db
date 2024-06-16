// Check if the browser supports the Web Audio API
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    let chunks = [];
    let mediaRecorder;

    const recordButton = document.getElementById('recordButton');
    const stopButton = document.getElementById('stopButton');
    const saveButton = document.getElementById('saveButton');

    recordButton.addEventListener('click', () => {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();

                mediaRecorder.ondataavailable = function(e) {
                    chunks.push(e.data);
                };

                mediaRecorder.onstop = function() {
                    const blob = new Blob(chunks, { 'type': 'audio/ogg; codecs=opus' });
                    chunks = [];
                    const audioURL = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.style.display = 'none';
                    a.href = audioURL;
                    a.download = 'audio.ogg';
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(audioURL);
                };

                recordButton.disabled = true;
                stopButton.disabled = false;
                saveButton.disabled = true;
            });
    });

    stopButton.addEventListener('click', () => {
        mediaRecorder.stop();
        recordButton.disabled = false;
        stopButton.disabled = true;
        saveButton.disabled = false;
    });

    saveButton.addEventListener('click', () => {
        stopButton.click();
    });
}
