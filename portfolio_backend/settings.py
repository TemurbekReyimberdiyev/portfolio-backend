import os
from pathlib import Path
from decouple import config
import dj_database_url

# 🔹 Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Maxfiy sozlamalar .env fayldan olinadi
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# 🔹 Backend subdomain va Render default domeni
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'api.temurbekreyimberdiev.uz',  # backend subdomain
    'yourapp.onrender.com',          # Render default subdomain
]

# 🔄 Django ilovalari
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'api',  # loyihadagi app
]

# 🔑 REST Framework JWT sozlamasi
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# ⚙️ Middleware — Whitenoise static fayllar uchun
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static fayllar uchun
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_backend.wsgi.application'

# 🗄️ Ma’lumotlar bazasi (PostgreSQL Render’dan)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600
    )
}

# 🔑 Parol validatsiyasi
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Til va vaqt
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🧱 Static fayllar
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 📁 Media fayllar
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 🌐 CORS (frontend domen bilan aloqa)
CORS_ALLOWED_ORIGINS = [
    "https://temurbekreyimberdiev.uz",       # frontend domain
    "https://www.temurbekreyimberdiev.uz",  # frontend www variant
    "http://localhost:5173",                 # lokal frontend
    "http://127.0.0.1:3000",                 # lokal frontend
]

# 🔑 Asosiy model kaliti
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
