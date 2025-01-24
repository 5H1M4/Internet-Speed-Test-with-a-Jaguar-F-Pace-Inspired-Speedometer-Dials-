// Test Data Simulation
function simulateSpeedTest(callback) {
    const results = {
      ping: Math.floor(Math.random() * 50) + 1, // Simulating ping
      download: (Math.random() * 100 + 50).toFixed(2), // Simulating download speed
      upload: (Math.random() * 50 + 10).toFixed(2), // Simulating upload speed
    };
  
    let progress = 0;
    const interval = setInterval(() => {
      progress += 10;
  
      // Updating dials in real-time
      if (progress <= 100) {
        document.getElementById("ping-value").innerText = `${results.ping}`;
        document.getElementById("download-value").innerText = `${(results.download * (progress / 100)).toFixed(2)}`;
        document.getElementById("upload-value").innerText = `${(results.upload * (progress / 100)).toFixed(2)}`;
      } else {
        clearInterval(interval);
        callback(results);
      }
    }, 300); // Update every 300ms
  }
  
  // Starting the Test
  document.getElementById("start-test").addEventListener("click", () => {
    const throttleButton = document.getElementById("start-test");
    throttleButton.style.display = "none"; // Hide throttle button during the test
  
    simulateSpeedTest((results) => {
      // Display results
      document.getElementById("result-ping").innerText = `${results.ping} ms`;
      document.getElementById("result-download").innerText = `${results.download} Mbps`;
      document.getElementById("result-upload").innerText = `${results.upload} Mbps`;
  
      // Show results panel
      document.getElementById("results-panel").classList.remove("hidden");
      document.getElementById("results-panel").style.display = "block";
    });
  });
  
  // Restart Test
  document.getElementById("restart-test").addEventListener("click", () => {
    document.getElementById("results-panel").style.display = "none";
    document.getElementById("start-test").style.display = "inline-block";
  
    // Reset dials
    document.getElementById("ping-value").innerText = "--";
    document.getElementById("download-value").innerText = "--";
    document.getElementById("upload-value").innerText = "--";
  });
  