"""
Django settings for {{ project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf.global_settings import *
from paths import *
import milieu
import os

#==============================================================================
# Environment settings
#==============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
M = milieu.init()
DEBUG = M.DEBUG or False
TEMPLATE_DEBUG = DEBUG

SITE_NAME = M.SITE_NAME or '{{ project_name }}'
SITE_DOMAIN = M.SITE_DOMAIN or 'localhost'
SITE_PORT = M.SITE_PORT or '5000'
FRONTENDS = (M.FRONTENDS or "http://localhost:5000").split(",")
ALLOWED_HOSTS = (M.ALLOWED_HOSTS or u'localhost').split(",")

#==============================================================================
# Generic Django project settings
#==============================================================================


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south'
)

PROJECT_APPS = (
    )

INSTALLED_APPS += PROJECT_APPS

ROOT_URLCONF = PROJECT_NAME + 'conf.urls'

#==============================================================================
# Static
#==============================================================================
if M.STORAGE_LOCAL or DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = PROJECT_NAME + '.conf.storage.StaticStorage'

STATIC_URL = '/static/' + PROJECT_NAME

STATIC_ROOT = os.path.join(VAR_ROOT, STATIC_URL )

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_NAME, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
#==============================================================================
# Media
#==============================================================================
if M.STORAGE_LOCAL or DEBUG:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
else:
    DEFAULT_FILE_STORAGE = PROJECT_NAME + '.conf.storage.MediaStorage'

MEDIA_URL = '/uploads/' + PROJECT_NAME

MEDIA_ROOT = os.path.join(VAR_ROOT, MEDIA_URL)

#==============================================================================
# Templates
#==============================================================================
TEMPLATE_LOADERS = (
   'django.template.loaders.filesystem.Loader',
   'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    # 'Custom context processors here',
    'django.core.context_processors.request',
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# Databases
#==============================================================================
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default="postgres://{{ project_name }}@localhost/{{ project_name }}")
}
#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================