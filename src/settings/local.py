# Development settings

from .base import *

SECRET_KEY = 'f41z(gp#mm7ktjo1bfux-n*0!mlti$9d1@k_sws@&kl*@tfi21'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sunset',  # postgres db name
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '0.0.0.0',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STRIPE_SECRET_KEY = 'sk_test_5BvPLqOw9Mlev8XxXN10qAdQ00ZP1E8a5T'
STRIPE_PUBLISHABLE_KEY = 'pk_test_P9hWMHFzKRfWHCOpgX0jsJbT00VKslhF2p'
