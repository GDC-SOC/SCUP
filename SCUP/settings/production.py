from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SETTINGS_JSON_PARSED['SECRET_KEY']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = SETTINGS_JSON_PARSED['ALLOWED_HOSTS']

try:
    from .local import *
except ImportError:
    pass
