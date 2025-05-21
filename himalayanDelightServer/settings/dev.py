from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-%=%grtsdw61dqr@u@_($+0sfc9pnk_l-lrg$v@1f(b(=1q-=b5'

ALLOWED_HOSTS = ['10.0.2.2', '127.0.0.1', 'localhost','192.168.2.205']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'himalayandelight',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':''
    }
}

# to run api locally
# python manage.py runserver 0.0.0.0:8000
# for ios
# python manage.py runserver 192.168.2.205:8000
