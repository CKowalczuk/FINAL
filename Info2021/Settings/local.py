from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'FINAL',
        'USER': 'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'5432',
    }
}