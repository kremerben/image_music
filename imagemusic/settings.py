"""
Django settings for imagemusic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't3sx(_2k5g*ji$dx5yl6gl@u3kxo)*vqwu=up&^(tyd&s+d%^2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['54.202.24.219']


# Application definition

INSTALLED_APPS = (
    'photosong',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'requests',
    'debug_toolbar',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'imagemusic.urls'

WSGI_APPLICATION = 'imagemusic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
# STATIC_URL = '/static/'

# MEDIA_URL = '/media/'
#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static-only')
STATIC_MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, "photosong/static", *MEDIA_URL.strip("/").split("/"))
MEDIA_ROOT = os.path.join(BASE_BASE_DIR, "static", *MEDIA_URL.strip("/").split("/"))
# MEDIA_ROOT = STATIC_MEDIA_ROOT

ADMINS = ('Ben','kremer.ads@gmail.com')
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kremer.ads@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'kremer.ads@gmail.com'


KAIROS_APP_ID = '467f2f67'
KAIROS_API_KEY = '727ff689667c548878e56369109af78f'

SOUNDCLOUD_CLIENT_ID = '00b06e88ddbb852fd7c6be9b9291b676'
SOUNDCLOUD_SECRET = '90b30c6e1ed1a47410cbc328011aae4c'

REKOGNITION_API_KEY = "U5TBVS2zxp8b7WoM"
REKOGNITION_API_SECRET = 'vKPn2LHkWHQKMUVK'

# AUTH_USER_MODEL = "similarity.User"


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    'static',
)

try:
    from local_settings import *
except ImportError:
    pass

#
# # Heroku settings
# # Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
#
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
# # Allow all host headers
# ALLOWED_HOSTS = ['*']
#
# # Static asset configuration
# import os
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
