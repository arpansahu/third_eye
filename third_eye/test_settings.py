"""
Test settings for third_eye project
Optimized for fast test execution with minimal dependencies
"""
from .settings import *

# Use SQLite for fast test execution
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Minimal middleware for testing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Disable password hashing for faster user creation in tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable Sentry in tests
import sentry_sdk
sentry_sdk.init(dsn=None)

# Use local storage in tests
USE_S3 = False
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'test_staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'test_media')

# Disable cache in tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Disable logging in tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}

# Debug mode for tests
DEBUG = True
ALLOWED_HOSTS = ['*']

# Faster template rendering
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
