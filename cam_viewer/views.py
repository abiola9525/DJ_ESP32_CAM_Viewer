from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    if request.method == 'POST':
        # If the form is submitted, get the IP address entered by the user
        ip_address = request.POST.get('ipAddress', '')
        
        # Fetch the camera feed from the provided IP address
        camera_feed_url = f"http://{ip_address}/mjpeg/1"
        response = requests.get(camera_feed_url, stream=True)
        
        if response.status_code == 200:
            # If the camera feed is fetched successfully, pass it to the template context
            camera_feed_content = response.content
        else:
            # If there's an error fetching the camera feed, set camera_feed_content to None
            camera_feed_content = None
    else:
        # If it's a GET request or if the form is not submitted, set camera_feed_content to None
        camera_feed_content = None
    
    # Pass camera_feed_content to the template context
    return render(request, 'index.html', {'camera_feed_content': camera_feed_content})


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


