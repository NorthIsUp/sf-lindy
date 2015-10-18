"""
Django settings for sflindy project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from __future__ import absolute_import

# External Libraries
from dj_database_url import config
from path import path

SFLINDY_DIR = path(__file__).abspath().dirname()
PROJECT_ROOT = (SFLINDY_DIR / '..' / '..').abspath()

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c8g!*be4@&o3qi%ia8*5=+46p^%nxmkz+po88b2em8tpxynw*@'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'pipeline',
    # 'djangobower',

    'sflindy',
    'portal',
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
                # 'pipeline.templatetags.ext.PipelineExtension',
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

PIPELINE_COMPILERS = (
    'react.utils.pipeline.JSXCompiler',
    'pipeline.compilers.sass.SASSCompiler',
)
PIPELINE_SASS_BINARY = '/usr/bin/env sassc'

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'pipeline.finders.PipelineFinder',
    # 'djangobower.finders.BowerFinder',
)

PIPELINE_CSS = {
    'ninetwenty': {
        'source_filenames': (
            'sass/*.sass',
        ),
        'output_filename': 'css/ninetwenty.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'jsx': {
        'source_filenames': (
            'jsx/*.jsx',
        ),
        'output_filename': 'js/app.js',
    }
}

BOWER_COMPONENTS_ROOT = PROJECT_ROOT / 'vendor'

BOWER_INSTALLED_APPS = (
    'underscore',
    'react-bootstrap',
)
