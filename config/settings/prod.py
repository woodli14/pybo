from .base import *

ALLOWED_HOSTS = ['15.164.144.141']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'databasetest',
        'HOST': 'ls-bf4b3f0faf60913c13492febe7fbf04387e7e718.c8z8uavkolp4.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

