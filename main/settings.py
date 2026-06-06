INSTALLED_APPS = [
    'django_azure_auth',        # <-- hinzufügen
    'django.contrib.auth'
]

# === Azure Auth Konfiguration ===
AZURE_AUTH = {
    "CLIENT_ID": "83fda9e9-9e0b-4360-a9c9-fcdbf73079cd",
    "CLIENT_SECRET": "e8373996-b66a-4aed-8cfb-3d119a12255f",
    "TENANT_ID": "common",        # "common" für alle Microsoft-Konten
    "REDIRECT_URI": "http://localhost:8000/accounts/microsoft/login/callback/",
    
    # Optional
    "CLIENT_TYPE": "confidential_client",   # Standard für Web-Apps mit Secret
    "SCOPE": ["openid", "profile", "email", "User.Read"]
}
