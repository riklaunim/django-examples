"""
Django settings for facebook_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'klzkdclfzqik*=r$s@=mf6rgwf(t+twypl+b*u+jinh%0w*!b9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'kombu.transport.django',
    'facebook_auth',
    'facebook_datastore',
    'facebook_javascript_sdk',
    'facebook_javascript_authentication',
    'facebook_signed_request',
    'javascript_settings',
    'social_metadata',
    'sslserver',
    'blog',
    'canvas_example',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'facebook_javascript_authentication.middlewares.P3PMiddleware',
    'facebook_signed_request.middleware.SignedRequestMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'facebook_signed_request.middleware.FacebookLoginMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'facebook_auth.backends.FacebookBackend',
    'facebook_auth.backends.FacebookJavascriptBackend',
)

ROOT_URLCONF = 'facebook_project.urls'

WSGI_APPLICATION = 'facebook_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_URL = 'http://localhost:8000'
STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/facebook_example/'
MEDIA_URL = 'http://localhost:8000/media/'
MEDIA_ROOT = 'media/'

FACEBOOK_APP_SECRET = 'SECRET_HERE'
FACEBOOK_APP_ID = 'APP_ID_HERE'
BROKER_URL = 'django://'
CELERY_ACCEPT_CONTENT = ['json']

import djcelery
djcelery.setup_loader()
