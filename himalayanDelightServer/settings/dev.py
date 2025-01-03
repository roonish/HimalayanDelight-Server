from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-%=%grtsdw61dqr@u@_($+0sfc9pnk_l-lrg$v@1f(b(=1q-=b5'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'himalayandelight',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':'ronish'
    }
}
