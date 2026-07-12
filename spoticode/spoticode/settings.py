from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]


# Application definition
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third Party Apps
    'django_admin_listfilter_dropdown',
    
    # Project Apps
    'spoticode.accounts',
    'spoticode.albums',
    'spoticode.artists',
    'spoticode.auditlog',
    'spoticode.common',
    'spoticode.playlists',
    'spoticode.songs',
    'spoticode.tasks',
    'spoticode.web',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Custom
    'spoticode.auditlog.middleware.CurrentUserMiddleware',
    'spoticode.web.middleware.DatabaseSelectorMiddleware',
]

ROOT_URLCONF = 'spoticode.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'spoticode.web.access_checkers.current_db',
            ],
        },
    },
]

WSGI_APPLICATION = 'spoticode.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME_DEFAULT'),
        'USER': os.environ.get('DB_USER_DEFAULT'),
        'PASSWORD': os.environ.get('DB_PASSWORD_DEFAULT'),
        'HOST': os.environ.get('DB_HOST_DEFAULT'),
        'PORT': os.environ.get('DB_PORT_DEFAULT'),
    },
    'spoticode_database': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME_0'),
        'USER': os.environ.get('DB_USER_0'),
        'PASSWORD': os.environ.get('DB_PASSWORD_0'),
        'HOST': os.environ.get('DB_HOST_0'),
        'PORT': os.environ.get('DB_PORT_0'),
    },
    'rock_database': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME_1'),
        'USER': os.environ.get('DB_USER_1'),
        'PASSWORD': os.environ.get('DB_PASSWORD_1'),
        'HOST': os.environ.get('DB_HOST_1'),
        'PORT': os.environ.get('DB_PORT_1'),
    },
    'balkan_database': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME_2'),
        'USER': os.environ.get('DB_USER_2'),
        'PASSWORD': os.environ.get('DB_PASSWORD_2'),
        'HOST': os.environ.get('DB_HOST_2'),
        'PORT': os.environ.get('DB_PORT_2'),
    },
    'pop_database': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME_3'),
        'USER': os.environ.get('DB_USER_3'),
        'PASSWORD': os.environ.get('DB_PASSWORD_3'),
        'HOST': os.environ.get('DB_HOST_3'),
        'PORT': os.environ.get('DB_PORT_3'),
    },
}

ACTIVE_DATABASES = ('spoticode_database', 'rock_database', 'balkan_database', 'pop_database')


DATABASE_ROUTERS = ['spoticode.web.routers.UserDBRouter']


# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / "static",
)


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
