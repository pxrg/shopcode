from unipath import Path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = Path(__file__).ancestor(2)

ADMINS = (
    ('Igor Santos', 'igr.exe@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'saas',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2',
}

ALLOWED_HOSTS = ['saas.io', '*.saas.io']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = BASE_DIR.child('img')

MEDIA_URL = '/img/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'as-%*_93v=r5*p_7cu8-%o6b&x^g+q$#*e*fl)k)x0-t=%q0qa'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'core.middleware.TenantTutorialMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'project.urls_tenants'
PUBLIC_SCHEMA_URLCONF = 'project.urls_public'

WSGI_APPLICATION = 'project.wsgi.application'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('staticfiles'),
)

TEMPLATE_DIRS = (
    BASE_DIR.child('templates'),
)

SHARED_APPS = (
    'tenant_schemas',
    # django apps
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third apps
    'south',
    'bootstrap3',
    # my apps
    'core',
)

TENANT_APPS = (
    # django apps
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    # third apps
    'south',
    'shop',
    'polymorphic',
    'shop.addressmodel',
    # my apps
    'qrshop',
)

TENANT_MODEL = "core.Client"

INSTALLED_APPS = TENANT_APPS + SHARED_APPS + ('tenant_schemas',)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Settings sending e-mail by Django
# https://docs.djangoproject.com/en/1.6/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'igr.exe@gmail.com'
EMAIL_HOST_PASSWORD = '5ybWxGzjxL_pe2DS1zn3UQ'
