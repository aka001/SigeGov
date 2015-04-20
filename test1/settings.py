"""
Django settings for test1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_d&l4q@o0vl(onoqfo&pf=t&g%5-+4vnk!+j+jlm1ka(-t*)fd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sigegov',
    'haystack',
    'registration',
    'social_auth',
    'djangoChat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test1.urls'

WSGI_APPLICATION = 'test1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eGov',
	'USER': 'root',
	'PASSWORD': 'ashish',
	'HOST': 'localhost',
	'PORT': '8000',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = False

WHOOSH_INDEX = os.path.join(BASE_DIR,'whoosh/')

HAYSTACK_CONNECTIONS = {
	'default' : {
		'ENGINE':  'haystack.backends.solr_backend.SolrEngine',
		'URL': 'http://127.0.0.1:8983/solr',
	},
}

#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

GOOGLE_OAUTH2_CLIENT_ID = '58874409849-lae2s3fo9hriq9560tsogv05fjh4kks7.apps.googleusercontent.com'

GOOGLE_OAUTH2_CLIENT_SECRET = 'nUe8d9t8QhahqHup9Wb-tdzL'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sigegov.gov@gmail.com'
EMAIL_HOST_PASSWORD = 'sigegov123'
DEFAULT_FROM_EMAIL = 'SigeGov'
EMAIL_PORT = 587

ACCOUNT_ACTIVATION_DAYS = 7

LOGIN_REDIRECT_URL = '/sigegov/'

#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/blood/'

AUTHENTICATION_BACKENDS = (
                        'social_auth.backends.google.GoogleOAuth2Backend',
                        'django.contrib.auth.backends.ModelBackend',
                        )

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)
STATIC_URL = '/static/'

AUTH_PROFILE_MODULE = "sigegov.UserProfile"
