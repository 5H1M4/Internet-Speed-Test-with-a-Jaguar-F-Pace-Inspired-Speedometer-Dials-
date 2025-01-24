from django.shortcuts import render
from speedtest import Speedtest
from django.http import JsonResponse
import time

def index(request):
    return render(request, 'dashboard.html')

def run_speedtest(request):
    if request.method == 'POST':
        st = Speedtest()
        start_time = time.time()
        
        download_speeds = []
        upload_speeds = []
        ping_values = []
        
        while time.time() - start_time < 10:
            download_speed = st.download() / (1024 * 1024)  # Convert to Mbps
            upload_speed = st.upload() / (1024 * 1024)      # Convert to Mbps
            ping_value = st.results.ping
            
            download_speeds.append(round(download_speed, 2))
            upload_speeds.append(round(upload_speed, 2))
            ping_values.append(round(ping_value, 2))
            
            time.sleep(0.5)  # Pause for 0.5 seconds
        
        data = {
            'download_speed': download_speeds[-1],
            'upload_speed': upload_speeds[-1],
            'ping': ping_values[-1],
            'max_download': max(download_speeds),
            'max_upload': max(upload_speeds),
            'min_ping': min(ping_values)
        }
        return Json