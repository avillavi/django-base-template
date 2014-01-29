from ..settings import *
from ..paths import PROJECT_NAME, PROJECT_DIR
from django.db import connections
import milieu

M = milieu.init()
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = PROJECT_NAME + '.conf.dev.urls'

MIDDLEWARE_CLASSES += (
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ('localhost')

INSTALLED_APPS += (
    'django_extensions',
)