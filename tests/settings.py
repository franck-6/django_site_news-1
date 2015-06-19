import logging
import os

import django

try:
    import honeypot
except ImportError:
    honeypot = None

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'iamasecretkeydonttellanyone'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'site_news'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'tests', 'templates'),
]

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'tests', 'fixtures'),)

ROOT_URLCONF = 'tests.urls'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

PASSWORD_HASHERS = {
    'django.contrib.auth.hashers.MD5PasswordHasher',
}

if django.VERSION[:2] < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'

logging.getLogger('site_news').addHandler(logging.NullHandler())

SOUTH_TESTS_MIGRATE = False
