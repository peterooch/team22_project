from .settings import *

# settings module for jenkins runs
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'django.sqlite3',
    },
}
