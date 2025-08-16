import os
from pathlib import Path
from decouple import config

# базовая леректория
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# секретный ключ безопасности
SECRET_KEY = config('SECRET_KEY')


# режим отладки
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS",default="").split(",")


# список встроенных проложение

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    "corsheaders",

]
LOCAL_APPS = [
    "apps.notes"

]
# ОБЩМЙ СПИСОК
INSTALLED_APPS  = THIRD_PARTY_APPS + INSTALLED_APPS + LOCAL_APPS


# СПИСОК МЕДЛВЕЙ ДЛЯ ОБРОБОТКИ ЗАПРОСОВ
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# КОРНЕВОЙ url ФАЙЛ ПРОЕКТ
ROOT_URLCONF = 'config.urls'


# КОНФЕГУРЯЦИЯ НАБЛОВО ДЖАНГО
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



# КОНФИГУРАЦИЯ ДАЗЫ ДАННЫХ
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB',default='modelhub'),
        'USER': config('POSTGRES_USER',default='postgresql'),
        'PASSWORD': config('POSTGRES_PASSWORD',default='passowrd'),
        'HOST': config('POSTGRES_HOST',default='localhost'),
        'PORT': config('POSTGRES_PORT',default='5432'),
        "ATOMIC_REQUESTS": True,
    }
}


# ВАЛИДАЦИЯ ПОРОЛЕЙ
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


# настройка интернациональности

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# настройка статических файлов

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# НАСТРОЙКИ ДЖАНГО REST FR


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':  [
        'rest_framework.permissions.AllowAny',
    ],
    "DEFAULT_THROTTLE_CLASSES": [
      "rest_framework.throttling.AnonRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon":"100/hour"
    },
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],

}

# настройка CORS для разработки и продакшена
if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",

    ]

# Настройки безопасности

SECURE_BROWSER_XSS_FILTER = True # Защита от xxs-атак
SECURE_CONTENT_TYPE_NOSNIFF = True # Запрет MINE - типов
X_FRAME_OPTIONS = 'DENY' # Защита от кликджекинга


# Настройка логирование
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file':{
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    "loggers": {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}



