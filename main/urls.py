from . import views
from django.contrib import admin
from django.urls import path, include
from main.views import home   # Home-View importieren

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Azure Auth URLs
    path('accounts/microsoft/login/', include('azure_auth.urls')),
    
    # Deine App
    path('', views.home, name="home"),  # Home-View für die Startseite
]