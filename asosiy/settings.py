from pathlib import Path
import os
import dj_database_url  # # CHANGED: Bazani DATABASE_URL orqali ulash uchun

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# # CHANGED: Xavfsizlik uchun kalitni muhitdan olamiz, topilmasa eskisini ishlatamiz
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-)_8a@0gr0sd2(v8_-3on&(1wn0v-48(0n9*j3p3=d2#jo2$&)6')

# # CHANGED: Render-da DEBUG har doim False bo'lishi kerak
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# # CHANGED: Render URL va lokal hostlarni qo'shish
ALLOWED_HOSTS = ['*'] 


# Application definition

INSTALLED_APPS = [
    'jazzmin',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kitoblarim',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # # CHANGED: Statik fayllar uchun
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'asosiy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # # CHANGED: templates papkasini tanish uchun
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

WSGI_APPLICATION = 'asosiy.wsgi.application'


# Database
# # CHANGED: Render-da PostgreSQL, lokalda SQLite ishlatadigan mantiq
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# Password validation
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


# Internationalization
LANGUAGE_CODE = 'uz-uz' # # CHANGED: O'zbek tiliga o'tkazildi

TIME_ZONE = 'Asia/Tashkent' # # CHANGED: O'zbekiston vaqti

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# # CHANGED: Statik va Media fayllar uchun to'liq sozlama
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# WhiteNoise uchun statik fayllarni siqish (Performance optimization)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'