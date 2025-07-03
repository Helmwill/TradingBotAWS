import os
import dj_database_url
from pathlib import Path

BASE_DIR - Path(__file__).resolve().parent.parent

SECRET_KEY = OS.getenv("DJANGO_SECRET_KEY", "your-default-secret")

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes'
    'django.contrib.staticfiles'
    'django.contrib.auth',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'trading_bot.urls'


DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

STATIC_URL = '/STATIC/'