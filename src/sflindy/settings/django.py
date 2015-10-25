from __future__ import absolute_import

# External Libraries
from dj_database_url import config
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

from .env import PROJECT_ROOT

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c8g!*be4@&o3qi%ia8*5=+46p^%nxmkz+po88b2em8tpxynw*@'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'djangobower',

    'sflindy',
    'lindy',
    'ninetwenty',

    # Debug
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sflindy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'sflindy.jinja2.environment',
            'extensions': [
                'pipeline.templatetags.ext.PipelineExtension',
            ]
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
            ],

        }
    }
]

WSGI_APPLICATION = 'sflindy.wsgi.application'

DATABASES = {
    'default': config('DATABASE_URL', default='sqlite:///db.sqlite3')
}

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True

STATIC_ROOT = PROJECT_ROOT / 'static'
STATIC_URL = '/static/'

APPEND_SLASH = True
