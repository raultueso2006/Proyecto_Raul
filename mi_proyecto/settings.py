"""
Configuración principal de Django para el proyecto 'mi_proyecto'.

Documentación oficial:
https://docs.djangoproject.com/en/5.2/topics/settings/
"""

from pathlib import Path
import os

# --------------------------------------------------------
# RUTAS Y CONFIGURACIÓN BÁSICA
# --------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!u)mmgqjqo!su7j1u(92qq%j4@jbp07$_14)7$%hgdo13(i)i8'

DEBUG = True  # ⚠️ Cambiar a False en producción
ALLOWED_HOSTS = []  # Agregar tu dominio o IP cuando despliegues el sitio

# --------------------------------------------------------
# APLICACIONES INSTALADAS
# --------------------------------------------------------
INSTALLED_APPS = [
    # Apps del sistema Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps personalizadas
    'recomendador',
    'usuarios',
    'catalogo',
]

# --------------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------------
# CONFIGURACIÓN DE URLs Y WSGI
# --------------------------------------------------------
ROOT_URLCONF = 'mi_proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Si querés usar plantillas globales (fuera de las apps), agregalas en una carpeta "templates" en la raíz del proyecto:
        'DIRS': [BASE_DIR / 'templates'],  
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

WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# --------------------------------------------------------
# BASE DE DATOS
# --------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------------
# VALIDADORES DE CONTRASEÑA
# --------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------
# INTERNACIONALIZACIÓN
# --------------------------------------------------------
LANGUAGE_CODE = 'es'          # Cambiado a español
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------
# ARCHIVOS ESTÁTICOS (CSS, JS, IMÁGENES DE LA APP)
# --------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'catalogo' / 'static']  # Ruta de tus CSS, JS, etc.
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Donde Django los recopila al hacer "collectstatic"

# --------------------------------------------------------
# ARCHIVOS MULTIMEDIA (IMÁGENES SUBIDAS POR USUARIOS)
# --------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------------
# AUTENTICACIÓN Y REDIRECCIONES
# --------------------------------------------------------
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# --------------------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'