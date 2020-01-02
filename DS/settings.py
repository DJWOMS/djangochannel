import os

from .ckeditor import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'djangochannel.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'debug_toolbar',
    'bootstrap4',
    'mptt',
    # docs
    'drf_yasg',
    # Editor
    'ckeditor',
    'ckeditor_uploader',

    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    # Auth
    'djoser',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',

    # my apps
    'backend.pages',
    'backend.blog',
    'backend.courses',
    'backend.forum',
    'backend.profile',
    'backend.dc_tests',
    'backend.reviews',
    'backend.moderation',
    'backend.pay',
    'backend.contact',
    'backend.message',
    'backend.dc_task',
    'backend.utils',
    'backend.followers',
    'backend.community',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'DS.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DATETIME_FORMAT': "%d.%m.%Y %H:%M:%S",
}


# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7)  # default
# }
#

# DJOSER = {
#     'SEND_ACTIVATION_EMAIL': True,
#     # 'SEND_CONFIRMATION_EMAIL': True,
#     'ACTIVATION_URL': 'auth/activate/{uid}/{token}/',
#     'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
#     'PASSWORD_RESET_CONFIRM_URL': 'auth/reset/confirm/{uid}/{token}/',
#     'TOKEN_MODEL': None
# }

# Allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_BLACKLIST = ["admin", "administrator", "moderator", "DjangoSchool"]
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'
# TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

INTERNAL_IPS = '127.0.0.1'

CORS_ORIGIN_ALLOW_ALL = True


MY_INFO = 80
MESSAGE_LEVEL = MY_INFO
MY_PRIVAT_MESS = 81
MESSAGE_LEVEL = MY_PRIVAT_MESS
TASK_MESS = 82
MESSAGE_LEVEL = TASK_MESS

# TODO Реализовать среду окружения
try:
    from .local_settings import *
except ImportError:
    try:
        from .prod_settings import *
    except ImportError:
        try:
            from .test_settings import *
        except ImportError:
            pass
