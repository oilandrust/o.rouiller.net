from orouiller.settings.common import *
import os

DEBUG = False

ALLOWED_HOSTS = ['orouiller.net','www.orouiller.net']

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/orouiller.net/media/'
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orouiller',
        'USER': 'ubuntu',
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


