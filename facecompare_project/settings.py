from pathlib import Path
import os  # ✅ Added to use os.getcwd() in MEDIA_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2kub2d%tza)()%@^@%*%+()ca358cg)_x(q0!458tlwj7tl0dr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ✅ Allow all hosts in development (you can replace '*' with your IP later)
ALLOWED_HOSTS = ['*']

# ✅ INSTALLED_APPS me compare (your app) aur corsheaders add karo
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',  # ✅ For CORS (frontend to call backend)
    'compare',      # ✅ Your face comparison app
]

# ✅ MIDDLEWARE me sabse upar corsheaders.middleware add karo
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ CORS should be at the top

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'facecompare_project.urls'

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

WSGI_APPLICATION = 'facecompare_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Media (face folders) serve karne ke liye config
MEDIA_URL = '/'
MEDIA_ROOT = os.getcwd()  # ✅ Serve files directly from current working dir

# ✅ Allow all origins to call this API (for development)
CORS_ALLOW_ALL_ORIGINS = True
