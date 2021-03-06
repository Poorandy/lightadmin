# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path
from dj_database_url import parse as db_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from pathlib import Path
import os
import sys

# 设置apps路径
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# load production server from .env
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]

INSTALLED_APPS += [
    'apps.app',  # Enable the inner app
    'apps.simc',
    'apps.core',
    'apps.plat',
    'django_celery_beat',
    'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + 'db.sqlite3',
        cast=db_url
    )
}

# celery
CELERY_BROKER_URL = config('REDIS_URL', default='redis://127.0.0.1:6379/0')
CELERY_RESULT_BACKEND = "django-db"
# 设置时间参照，不设置默认使用的UTC时间
CELERY_TIMEZONE = 'Asia/Shanghai'
# 指定任务的序列化
CELERY_TASK_SERIALIZER = 'json'
# 指定执行结果的序列化
CELERY_RESULT_SERIALIZER = 'json'
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'core/static'),
)

#############################################################
#############################################################

X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']

# simleui configs
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'dynamic': True,
    'menus': [{
        'app': 'auth',
        'name': 'AUTH',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': 'USER',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        },
            {
                'name': 'GROUP',
                'icon': 'fa fa-users',
                'url': 'auth/group'
            }]
    }, {
        # 'app': 'apps.',
        'name': 'SETTINGS',
        'icon': 'fa fa-cogs',
        'models': [{
            'name': 'MONSTERS',
            'icon': "fab fa-optin-monster",
            'url': 'simc/monster/'
        }, {
            'name': 'CARDS',
            'icon': "fas fa-money-bill",
            'url': 'simc/card/'
        }, {
            'name': 'CHARACTER',
            'icon': 'fas fa-hamsa',
            'url': 'simc/character/'
        }, {
            'name': 'DUNGEON',
            'icon': 'fas fa-dungeon',
            'url': 'simc/battlefield'
        }, {
            'name': 'AURA',
            'icon': 'fas fa-sun',
            'url': 'simc/aura'
        },{
            'name': 'ARMOR&ARMS',
            'icon': 'fas fa-shield-alt',
            'url': 'simc/armorarms'
        }]

    }]
}

SIMPLEUI_HOME_INFO = False

# SIMPLEUI_LOGO = 'https://miro.com/api/v1/accounts/3074457358670303205/picture?etag=R3074457346012449852_1&size=140'
