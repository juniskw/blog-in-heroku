#!/usr/bin/env python
#coding:utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ik%o4=nfzaq9tte1t4)_l%0%u)t4ws=8dde*au&j@rhscut60q'

#jj
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
#jj

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fastblog.urls'

WSGI_APPLICATION = 'fastblog.wsgi.application'


# Database
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

#jjj
STATIC_ROOT = 'staticfiles'
#jjj
STATIC_URL = '/static/'
#jjj
STATICFILES_DIRS = {
	os.path.join(BASE_DIR,'static'),
}
#jjji


## Sentry

INSTALLED_APPS = INSTALLED_APPS + (
	'raven.contrib.django.raven_compat',
)

from raven.contrib.django.models import client
from raven.base import Client

client = Client()

try:
	1/0
except Exception:
	client.captureException()
