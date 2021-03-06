#!/usr/bin/env python
#coding:utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))	# os.path.dirname( os.path.abspath(__file__) )


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
	 'fastblog.page_of_fastblog',
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

TEMPLATE_DIRS = (
	 os.path.join(BASE_DIR,'templates'),
)

# Database

#import dj_database_url

DATABASES = {
	 'default': {
		 'ENGINE':u'django.db.backends.postgresql_psycopg2',
		 'NAME':'d1josmcc6nebsf',
		 'USER':'dwduxqyceejlnu',
		 'PASSWORD':'EuF1C1it_T2U3nPLJjFj0Q3uRA',
		 'HOST':'ec2-54-197-241-78.compute-1.amazonaws.com',
		 'PORT':'5432',
	 },
}
"""
DATABASES = {
	 'default': {
		 'ENGINE':u'django.db.backends.sqlite3',
		 'NAME':'fastblog.sqlite',
	 },
}
"""
#DATABASES['default'] = dj_database_url.config()

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

#jjj
STATIC_ROOT = 'staticfiles'
#jjj
STATIC_URL = '/static/'
#jjj
STATICFILES_DIRS = (
	os.path.join(BASE_DIR,'static'),
)
