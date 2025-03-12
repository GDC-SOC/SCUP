"""
Django settings for SCUP project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, json

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SETTINGS_JSON = os.path.join(BASE_DIR, 'SCUP', 'settings', 'settings_new.json')
with open(SETTINGS_JSON) as settings_f:
    SETTINGS_JSON_PARSED = json.load(settings_f)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "home",
    "data",
    "instrument",
    "search",
    "wagtailvideos",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "wagtail.api.v2",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
    "rest_framework",
    "wagtail.contrib.table_block",
    "objectives",
    'django_otp',
    'django_otp.plugins.otp_totp',  # Time-based OTP (Google Authenticator)
    'django_otp.plugins.otp_static',  # Backup codes
    'django_otp.plugins.otp_email',  # Email-based OTP (optional)
    'mfa',
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware", 
    'django_otp.middleware.OTPMiddleware',  # Add OTP Middleware
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    'SCUP.middleware.EnforceAdmin2FA'
]

# AUTHENTICATION_BACKENDS = [
#     # 'django_otp.backends.OTPBackend',  # Ensures OTP authentication is processed
#     'django.contrib.auth.backends.ModelBackend',  # Keeps Django's default authentication
# ]

AUTHENTICATION_BACKENDS = [
    # "mfa.backends.MFAAuthBackend",  # MFA authentication backend
    "django.contrib.auth.backends.ModelBackend",  # Default authentication backend
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_URL = 'two_factor:login'

ROOT_URLCONF = "SCUP.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "SCUP.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": SETTINGS_JSON_PARSED["ENGINE"], 
        "NAME": SETTINGS_JSON_PARSED["PGDB"],
        "USER": SETTINGS_JSON_PARSED["PGUSER"],
        "PASSWORD": SETTINGS_JSON_PARSED["PGPASS"],
        "HOST": SETTINGS_JSON_PARSED["PGHOST"],
        "PORT": SETTINGS_JSON_PARSED["PGPORT"],
}}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "SCUP"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://gdc.smce.nasa.gov"

CSRF_TRUSTED_ORIGINS = SETTINGS_JSON_PARSED["CSRF_TRUSTED_ORIGINS"]


# Setting up logging
# This configuration log messages of INFO level or above.
# The log messages will be formatted with the timestamp,
# log level, and message. The logging will be directed to
# a log file located at /app/logs/davinci_website.log inside the Docker
# container.

# Ensure that the required modules have been imported
import os
import datetime
import logging

# Define the path for the logs directory
logs_directory = os.path.join(BASE_DIR, 'logs')

# Create the logs directory if it doesn't already exist
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

# Define the format string for the timestamp
format_str = '%j %Y-%m-%d %H:%M:%S,%f'
milliseconds = datetime.datetime.now().strftime('%f')[:-3]  # Extract milliseconds

# Append the milliseconds to the format string
format_str_with_ms = format_str.replace('%f', milliseconds)

# Configure logging
log_file_path = os.path.join(logs_directory, 'django_SCUP.log')

print(f"Creating log at {log_file_path}") 
logging.basicConfig(
    handlers=[
        logging.FileHandler(log_file_path, encoding='utf-8'),
    ],
    level="DEBUG",
    format='%(asctime)s UTC %(levelname)s: %(message)s',
    datefmt=format_str_with_ms
)
# Log a message to confirm that logging is working
logging.debug('Logging is working. Get back to work.')