"""
Django settings for openduty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType
djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

BROKER_URL = 'django://'

LOGIN_URL = '/login/'

PROFILE_MODULE = 'openduty.UserProfile'


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'kombu.transport.django',
    'openduty',
    'openduty.templatetags',
    'schedule',
    'djcelery',
    'notification',
    'django_tables2',
    'django_tables2_simplefilter',
    'bootstrap3',
    "django_twilio"
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'openduty.urls'

WSGI_APPLICATION = 'openduty.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIRST_DAY_OF_WEEK = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 10
}

PAGINATION_DEFAULT_PAGINATION = 20 # The default amount of items to show on a page if no number is specified.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT =  os.path.realpath(os.path.dirname(__file__))+"/static/"
STATICFILES_DIRS = (
    os.path.realpath(os.path.dirname(__file__))+'/static_schedule/',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

AUTH_PROFILE_MODULE = 'openduty.UserProfile'

BASE_URL = "http://52.87.147.52:8000"

XMPP_SETTINGS = {
}

EMAIL_SETTINGS = {
    'user': "gu3sss@gmail.com",
    'password': "Prashtuls@9"
}

TWILIO_SETTINGS = {
    'SID': "ACa388ccebaea03bb36f9b1ef1de1617af",
    'token': "869f7d0044468a5aab446b24f98cd949",
    'phone_number': "+12109085879",
    'sms_number': "+12109085879",
    'twiml_url': "https://github.com/gu3sss/openduty/blob/master/extra/voice.xml"
}

SLACK_SETTINGS = {
    'apikey': "xoxb-202995176103-72JVqdD9ZjVVzAjBcHLAWTAm"
}

PROWL_SETTINGS = {
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
}
TWILIO_ACCOUNT_SID = TWILIO_SETTINGS.get("SID", "disabled")
TWILIO_AUTH_TOKEN = TWILIO_SETTINGS.get("token", "disabled")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'devsecret'

import sys
if 'test' in sys.argv:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'openduty',
        'USER': 'openduty',
        'PASSWORD': 'dutyfree',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
}


    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATIC_SCHEDULE_URL = '/static_schedule/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
