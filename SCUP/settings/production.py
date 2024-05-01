from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings_secrets_client.secret_key

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = settings_secrets_client.allowed_hosts

try:
    from .local import *
except ImportError:
    pass
