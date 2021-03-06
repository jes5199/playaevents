import os

DIRNAME = os.path.dirname(__file__)
_parent = lambda x: os.path.normpath(os.path.join(x, '..'))
PARENT_DIRNAME = _parent(DIRNAME)

ADMINS = (
    ('Bruce Kroeze', 'bruce@ecomsmith.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = os.path.join(DIRNAME, 'media')
STATIC_ROOT = os.path.join(DIRNAME, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Don't share this with anybody.
SECRET_KEY = 'h7ny60*1c8(%4h(0c8@470sg$&1$m5jae*z(+m9ck3*!f%i91o'

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'playaevents.api.middleware.ContentTypeMiddleware',
    'playaevents.middleware.LoggedInMiddleware'
)

ROOT_URLCONF = 'playaevents.urls'

ACCOUNT_ACTIVATION_DAYS = 14
AUTH_PROFILE_MODULE = 'bmprofile.BmProfile'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'playaevents',
    'playaevents.api',
    'swingtime',
    'south',
    'django_extensions',
    'keyedcache',
    'registration',
    'bmprofile',
    'signedauth',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'playaevents.context_processors.add_keys',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(PARENT_DIRNAME, "templates"),
)

CACHE_LOCATION = os.path.join(PARENT_DIRNAME, 'cache')
if not os.path.exists(CACHE_LOCATION):
    os.mkdir(CACHE_LOCATION)

CACHES = {
    'default' : {
        'BACKEND' : 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION' : CACHE_LOCATION,
        'TIMEOUT' : 60*60*6 # 6 hours
        }
    }

CACHE_PREFIX = 'F'
CACHE_TIMEOUT = 60*60*24

DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False }

LOGGED_IN_ONLY = False

from settings_local import *

log.debug('running with DB %s', DATABASE_ENGINE)
