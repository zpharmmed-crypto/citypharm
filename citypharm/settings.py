import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY берём из переменных окружения (на Render задаём вручную)
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-local-default")

# DEBUG: по умолчанию False в проде
DEBUG = False

# ALLOWED_HOSTS: можно задавать через переменную, либо разрешить все (для теста)
ALLOWED_HOSTS = ['*']

# CSRF: разрешаем домены Render/ngrok если понадобятся
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
    "https://*.up.railway.app",
    "https://*.ngrok-free.dev",
]

# Приложения (включи свои)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # твои приложения
    'branches',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # для статики
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'citypharm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # если используешь общие templates
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

WSGI_APPLICATION = 'citypharm.wsgi.application'

# DATABASE: используем DATABASE_URL (Render даст нам)
DATABASES = {
    'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}

# Пароли и остальное — оставляем как есть
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# СТАТИКА
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Whitenoise оптимально обслуживает статику
STATICFILES_DIRS = [BASE_DIR / 'static']  # если есть
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')