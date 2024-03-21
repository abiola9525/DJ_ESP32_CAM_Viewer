function connectCamera() {
    var ipAddress = document.getElementById('ipAddress').value;
    var cameraFeedUrl = "http://" + ipAddress + "/mjpeg/1";

    // Update video source
    document.getElementById('cameraFeed').innerHTML = '<img src="' + cameraFeedUrl + '">';

    // Show timer
    document.getElementById('timestamp').style.display = 'block';

    // Start capturing screenshots every 3 seconds
    setInterval(captureScreenshot, 3000);
}



function captureScreenshot() {
    // Dummy function for demonstration
    console.log("Capturing screenshot...");
}

// Update timestamp every second
setInterval(updateTimestamp, 1000);

function updateTimestamp() {
    var now = new Date();
    var timestamp = now.toLocaleTimeString();
    document.getElementById('timestamp').innerText = "Current Time: " + timestamp;
}
