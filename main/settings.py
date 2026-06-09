import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'azure_auth',      # ← wichtig
    'main',                # deine App
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL="static/"
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# === Azure Auth Konfiguration ===
AZURE_AUTH = {
    "CLIENT_ID": os.getenv("CLIENT_ID"),
    "CLIENT_SECRET": os.getenv("CLIENT_SECRET"),
    "TENANT_ID": os.getenv("TENANT_ID"),
    "REDIRECT_URI": "http://localhost:8000/accounts/microsoft/login/callback",
    "USERNAME_ATTRIBUTE": "preferred_username",
    "AUTHORITY": f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}",
    "PROMPT": "login",
    
    # Optional
    "CLIENT_TYPE": "confidential_client",   # Standard für Web-Apps mit Secret
    "SCOPES": ["User.Read", "email"]
}
LOGIN_URL = "/azure_auth/login"
LOGIN_REDIRECT_URL = "/"
AUTHENTICATION_BACKENDS = ("azure_auth.backends.AzureBackend",)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }   
}
