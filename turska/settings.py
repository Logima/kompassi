# encoding: utf-8
from __future__ import absolute_import

import os
from datetime import datetime, timedelta

from django.utils.translation import ugettext_lazy as _

def mkpath(*parts):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', *parts))


MKPATH = mkpath

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_URLS_REGEX = r'^/(api|oauth2)/.*$'
CORS_ORIGIN_WHITELIST = (
    # Add any applications that need CORS for the API here
    # 'kirppu.tracon.fi',
)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kompassidev',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Uncomment if you have memcached
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': [
#             '127.0.0.1:11211'
#         ]
#     }
# }

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Helsinki'
DATETIME_FORMAT = SHORT_DATETIME_FORMAT = 'd.m.Y H:i'
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('fi', _('Finnish')),
    ('en', _('English')),
    # and all the other languages you have translated.
)
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = mkpath('media')
MEDIA_URL = '/media/'
STATIC_ROOT = mkpath('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'jhdjl*kxcet2aaz)%ixmois*j_p+d*q79%legoz+9el(c%zc$%'

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.PageWizardMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'turska.urls'
WSGI_APPLICATION = 'turska.wsgi.application'
APPEND_SLASH = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            mkpath('turska','templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'core.context_processors.core_context',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
            ],
            'loaders': [
                ('pyjade.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': ['pyjade.ext.django.templatetags'],
        },
    },
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'pyjade.ext.django',
    'crispy_forms',
    'oauth2_provider',
    'nexmo',

    'core',
    'programme',
    'labour',
    'labour_common_qualifications',
    'tickets',
    'payments',
    'mailings',
    'api',
    'api_v2',
    'badges',
    'access',
    'sms',
    'membership',

    # Uncomment if you have Atlassian Crowd
    # 'crowd_integration',

    # Uncomment if you do PDF tickets
    'lippukala',

    # Uncomment if you have Celery
    # 'background_tasks',

    'branding',
    'desuprofile_integration',

    'events.tracon8',
    'events.tracon9',
    'events.kawacon2014',
    'events.concon9',
    'events.traconx',
    'events.hitpoint2015',
    'events.yukicon2015',
    'events.kuplii2015',
    'events.popcult2015',
    'events.mimicon2015',
    'events.animecon2015',
    'events.popcultday2015',
    'events.yukicon2016',
    'events.finncon2016',
    'events.frostbite2016',
    'events.tracon11',
    'events.kuplii2016',
    'events.aicon2016',
    'events.popcult2016',
    'events.ropecon2016',
    'events.kawacon2016',
    'events.mimicon2016',
    'events.desucon2016',
    'events.lakeuscon2016',
    'events.animecon2016',

    'organizations.tracon_ry',
    'organizations.aicon_ry',
    'organizations.yukitea_ry',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'celery': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
        'kompassi': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
        'requests': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
    }
}

LOGIN_URL = '/login'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

DATE_FORMAT = 'j.n.Y'
DATE_FORMAT_STRFTIME = '%d.%m.%Y'

DATETIME_FORMAT = 'j.n.Y G:i:s'
DATETIME_FORMAT_STRFTIME = '%d.%m.%Y %H:%M:%S'


KOMPASSI_APPLICATION_NAME = u'Kompassi'
KOMPASSI_INSTALLATION_NAME = u'Kompassi (DEV)'
KOMPASSI_INSTALLATION_NAME_ILLATIVE = u'Kompassin kehitys\u00ADinstanssiin'
KOMPASSI_INSTALLATION_NAME_GENITIVE = u'Kompassin kehitys\u00ADinstanssin'
KOMPASSI_INSTALLATION_NAME_PARTITIVE = u'Kompassin kehitys\u00ADinstanssia'
KOMPASSI_INSTALLATION_SLUG = 'turskadev'
KOMPASSI_PRIVACY_POLICY_URL = 'http://media.tracon.fi/2014/tracon9_turska_rekisteriseloste.pdf'

# Confluence & co. require a group of users
KOMPASSI_NEW_USER_GROUPS = ['users']

AUTHENTICATION_BACKENDS = (
    'core.backends.KompassiImpersonationBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# These MUST match those in IPA
KOMPASSI_PASSWORD_MIN_LENGTH = 8
KOMPASSI_PASSWORD_MIN_CLASSES = 3

# Don't actually send email
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
DEFAULT_FROM_EMAIL = 'suunnistajat@kompassi.eu'


if 'payments' in INSTALLED_APPS:
    from payments.defaults import CHECKOUT_PARAMS


if 'lippukala' in INSTALLED_APPS:
    import tickets.lippukala_integration

    LIPPUKALA_PREFIXES = tickets.lippukala_integration.PREFIXES
    LIPPUKALA_LITERATE_KEYSPACES = tickets.lippukala_integration.KEYSPACES

    LIPPUKALA_CODE_MIN_N_DIGITS = 7
    LIPPUKALA_CODE_MAX_N_DIGITS = 7

    # NOTE these will be overridden by the respective fields in TicketsEventMeta
    # however, they need to be defined in settings or lippukala will barf.
    LIPPUKALA_PRINT_LOGO_PATH = mkpath('events', 'popcult2016', 'static', 'images', 'popcult.png')
    LIPPUKALA_PRINT_LOGO_SIZE_CM = (3.0, 3.0)


if 'background_tasks' in INSTALLED_APPS:
    BROKER_URL = 'amqp://{KOMPASSI_INSTALLATION_SLUG}:{KOMPASSI_INSTALLATION_SLUG}@localhost/{KOMPASSI_INSTALLATION_SLUG}'.format(**locals())
    CELERY_ACCEPT_CONTENT = ['json']

    #EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

    CELERY_SEND_TASK_ERROR_EMAILS = not DEBUG
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'


if 'api' in INSTALLED_APPS:
    KOMPASSI_APPLICATION_USER_GROUP = '{KOMPASSI_INSTALLATION_SLUG}-apps'.format(**locals())


if 'api_v2' in INSTALLED_APPS:
    AUTHENTICATION_BACKENDS = (
        'oauth2_provider.backends.OAuth2Backend',
    ) + AUTHENTICATION_BACKENDS

    OAUTH2_PROVIDER = dict(
        SCOPES=dict(
            read=u'Tietää nimesi, sähköpostiosoitteesi, puhelinnumerosi ja syntymäaikasi',
            write=u'Muokata käyttäjä- ja henkilötietojasi',
        )
    )


if 'nexmo' in INSTALLED_APPS:
    NEXMO_USERNAME = 'username'
    NEXMO_PASSWORD = 'password'
    NEXMO_FROM = 'Name or number'
    NEXMO_INBOUND_KEY = '0123456789abcdef'


if 'branding' in INSTALLED_APPS:
    KOMPASSI_ACCOUNT_BRANDING = u'Kompassi-tunnus'
    KOMPASSI_ACCOUNT_BRANDING_PARTITIVE = u'Kompassi-tunnusta'
    KOMPASSI_ACCOUNT_BRANDING_GENITIVE = u'Kompassi-tunnuksen (ent. Tracon-tunnuksen)'
    KOMPASSI_ACCOUNT_BRANDING_ADESSIVE = u'Kompassi-tunnuksella'
    KOMPASSI_ACCOUNT_BRANDING_2ND_PERSON_ADESSIVE = u'Kompassi-tunnuksellasi'


if 'crowd_integration' in INSTALLED_APPS:
    KOMPASSI_CROWD_APPLICATION_NAME = 'kompassidev'
    KOMPASSI_CROWD_APPLICATION_PASSWORD = 'secret'
    KOMPASSI_CROWD_HOST = 'https://crowd.tracon.fi'
    KOMPASSI_CROWD_BASE_URL = '{host}/crowd/rest/usermanagement/1'.format(host=KOMPASSI_CROWD_HOST)


if 'desuprofile_integration' in INSTALLED_APPS:
    KOMPASSI_DESUPROFILE_HOST = 'https://desucon.fi'
    KOMPASSI_DESUPROFILE_OAUTH2_CLIENT_ID = 'kompassi_insecure_client_id'
    KOMPASSI_DESUPROFILE_OAUTH2_CLIENT_SECRET = 'kompassi_insecure_client_secret'
    KOMPASSI_DESUPROFILE_OAUTH2_SCOPE = ['read']
    KOMPASSI_DESUPROFILE_OAUTH2_AUTHORIZATION_URL = '{KOMPASSI_DESUPROFILE_HOST}/oauth2/authorize/'.format(**locals())
    KOMPASSI_DESUPROFILE_OAUTH2_TOKEN_URL = '{KOMPASSI_DESUPROFILE_HOST}/oauth2/token/'.format(**locals())
    KOMPASSI_DESUPROFILE_API_URL = '{KOMPASSI_DESUPROFILE_HOST}/api/user/me/'.format(**locals())
