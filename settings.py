import os
from openslides.global_settings import *

OPENSLIDES_USER_DATA_DIR = '/root/.local/share/openslides'

INSTALLED_PLUGINS += (
#    'plugin_module_name',
)

INSTALLED_APPS += INSTALLED_PLUGINS


SECRET_KEY = os.getenv('OPENSLIDES_SECRET', 'verySecret')

DEBUG = False

RESET_PASSWORD_VERBOSE_ERRORS = True

EMAIL_HOST = os.getenv('OPENSLIDES_EMAIL_HOST', 'localhost')
EMAIL_PORT = os.getenv('OPENSLIDES_EMAIL_PORT', '587')
EMAIL_HOST_USER = os.getenv('OPENSLIDES_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('OPENSLIDES_EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.getenv('OPENSLIDES_DEFAULT_FROM_EMAIL', 'noreply@example.com')

# Increasing Upload size to 100mb (default is 2.5mb)
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(OPENSLIDES_USER_DATA_DIR, 'db.sqlite3'),
    }
}


# Set use_redis to True to activate redis as cache-, asgi- and session backend.
use_redis = False

if use_redis:

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("localhost", 6379)],
                "capacity": 100000,
            },
        },
    }

    REDIS_ADDRESS = "redis://127.0.0.1"


    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS = {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
        'prefix': 'session',
        'socket_timeout': 2
    }

ENABLE_SAML = False
if ENABLE_SAML:
    INSTALLED_APPS += ['openslides.saml']


TIME_ZONE = 'Europe/Berlin'

STATICFILES_DIRS = [os.path.join(OPENSLIDES_USER_DATA_DIR, 'static')] + STATICFILES_DIRS

STATIC_ROOT = os.path.join(OPENSLIDES_USER_DATA_DIR, 'collected-static')


MEDIA_ROOT = os.path.join(OPENSLIDES_USER_DATA_DIR, 'media', '')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'gunicorn': {
            'format': '{asctime} [{process:d}] [{levelname}] {name} {message}',
            'style': '{',
            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'gunicorn',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'openslides': {
            'handlers': ['console'],
            'level': os.getenv('OPENSLIDES_LOG_LEVEL', 'INFO'),
        }
    },
}

SETTINGS_FILEPATH = __file__