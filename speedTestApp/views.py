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
        
        # Collect data over 10 seconds
        while time.time() - start_time < 10:
            download = st.download() / (1024 * 1024)  # Convert to Mbps
            upload = st.upload() / (1024 * 1024)      # Convert to Mbps
            ping = st.results.ping
            
            download_speeds.append(round(download, 2))
            upload_speeds.append(round(upload, 2))
            ping_values.append(round(ping, 2))
            
            time.sleep(0.5)  # Pause for 0.5 seconds
        
        data = {
            'download_speeds': download_speeds,
            'upload_speeds': upload_speeds,
            'ping_values': ping_values,
            'max_download': max(download_speeds),
            'max_upload': max(upload_speeds),
            'min_ping': min(ping_values),
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)