from django.contrib import admin
import main.views as views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('accounts/microsoft/login/', include('azure_auth.urls')),  # Azure Auth URLs einbinden
    path('', views.home, name="home"),  # Home-View für die Startseite
]