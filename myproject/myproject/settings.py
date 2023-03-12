# Dummy Django settings

DEBUG = True

ALLOWED_HOSTS = ['localhost']

SECRET_KEY = 'fake_secret_key'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dummy_db.sqlite3',
    }
}

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# End of dummy Django settings

