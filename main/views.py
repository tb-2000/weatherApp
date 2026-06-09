from django.shortcuts import render
from azure_auth.decorators import azure_auth_required
import datetime

# Mock Wetterdaten (später durch echte API ersetzen)
def get_mock_weather(city="Berlin"):
    return {
        "city": city,
        "temperature": 18,
        "condition": "Leicht bewölkt",
        "humidity": 65,
        "wind": 12,
        "icon": "☁️",
        "last_updated": datetime.datetime.now().strftime("%H:%M Uhr")
    }

def home(request):
    return render(request, 'home.html')

@azure_auth_required
def dashboard(request):
    weather = get_mock_weather("Berlin")
    context = {
        'weather': weather,
        'user': request.user,
    }
    return render(request, 'index.html', context)

# Beispiel: Wetter für andere Stadt
@azure_auth_required
def weather_city(request, city):
    weather = get_mock_weather(city)
    context = {
        'weather': weather,
        'user': request.user,
    }
    return render(request, 'index.html', context)