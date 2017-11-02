"""
Django settings for uni_ddns project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
KEY_PATH = "../settings/uni_ddns/"
with open(os.path.join(BASE_DIR, KEY_PATH, 'sec_key')) as f:
    SECRET_KEY = f.read().strip()

PGRES_DICT = {}
with open(os.path.join(BASE_DIR, KEY_PATH, 'pgres_key')) as f:
    for line in f:
        (key, val) = line.split()
        PGRES_DICT[str(key)] = val

SETTINGS_DICT = {}
with open(os.path.join(BASE_DIR, KEY_PATH, 'settings')) as f:
    for line in f:
        (key, val) = line.split()
        SETTINGS_DICT[str(key)] = val

BLACK_LIST = []
with open(os.path.join(BASE_DIR, KEY_PATH, 'zone_blacklist')) as f:
    for line in f:
        BLACK_LIST.append(line.rstrip())

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.path.isfile(os.path.join(BASE_DIR, KEY_PATH, 'debug'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'verbose'
        },
        'file-debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filters': ['require_debug_true'],
            'filename': os.path.join(BASE_DIR, SETTINGS_DICT['LOGFILE_RELPATH'], "django-debug.log"),
            'formatter': 'verbose',
        },
        'file-default': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filters': ['require_debug_false'],
            'filename': os.path.join(BASE_DIR, SETTINGS_DICT['LOGFILE_RELPATH'], "django.log"),
            'formatter': 'simple'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file-default', 'file-debug', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ALLOWED_HOSTS = []
with open(os.path.join(BASE_DIR, KEY_PATH, 'hosts')) as f:
    for line in f:
        ALLOWED_HOSTS.append(line.strip())

STATIC_DICT = {}
with open(os.path.join(BASE_DIR, KEY_PATH, 'static')) as f:
    for line in f:
        (key, val) = line.split()
        STATIC_DICT[str(key)] = val

# Application definition

INSTALLED_APPS = [
    'ddns_query.apps.DdnsQueryConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uni_ddns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'uni_ddns.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PGRES_DICT['NAME'],
        'USER': PGRES_DICT['USER'],
        'PASSWORD': PGRES_DICT['PASSWORD'],
        'HOST': PGRES_DICT['HOST'],
        'PORT': PGRES_DICT['PORT'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'ddns_query.User'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

STATIC_ROOT = STATIC_DICT['ROOT']

STATIC_URL = STATIC_DICT['URL']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
if DEBUG is False:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_HTTPONLY = True
    X_FRAME_OPTIONS = 'DENY'
