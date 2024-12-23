"""
Django settings for posyandu project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z6_m1@nd@4&ae#a6eh&kaugsex&d&g7-2lqx@%(l(nq1b=-l&5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history", 
    'anggota',
    'db_bayi',
    'db_jentik',
    'jadwal_kegiatan',
    'jadwal_kunjungan',
    'kotaksaran',
    'posyandu',
    'sarpras',
    'admincode',
    'db_ibuhamil',
    'db_imunisasi',
    'db_posbindu',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # installed apps
    "django_extensions",
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'posyandu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'posyandu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "posyandu",
        "USER": "postgres",
        "PASSWORD": "12345678",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_TITLE": "Posyandu Bunga Tulip",
    "SITE_HEADER": "Posyandu Bunga Tulip",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("assets/logo.png"),  # light mode
        "dark": lambda request: static("assets/logo.png"),  # dark mode
    },

    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
          "navigation" : [
               {
                "title":"Navigation",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"Dashboard",
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        # "badge": "sample_app.badge_callback",
                        "permission": lambda request: request.user.is_superuser,
                    },      
                ],
                },
                {
                "title":"Admins",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"Admin - Group",
                        "icon": "admin_panel_settings",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title":"Admin - User",
                        "icon": "admin_panel_settings",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },             
                  ],
                },
                {
                "title":"Anggota Posyandu",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"Anggota",
                        "icon": "people",
                        "link": reverse_lazy("admin:anggota_anggotaposyandu_changelist"),
                    },
                  ],
                },
                {
                "title":"Daftar Bayi",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"Bayi",
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:db_bayi_bayi_changelist"),
                    },
                  ],
                },
                {
                "title":"Daftar ibu hamil",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"Ibu Hamil",
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:db_ibuhamil_ibuhamil_changelist"),
                    },
                  ],
                },
                {
                "title":"Daftar imunisasi",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"imunisasi",
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:db_imunisasi_imunisasi_changelist"),
                    },
                  ],
              },
                {
                "title":"Daftar posbindu",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"list posbindu",
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:db_posbindu_posbindu_changelist"),
                    },
                  ],
              },
                {
                "title":"jadwal kegiatan",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"jadwal",
                        "icon": "schedule",
                        "link": reverse_lazy("admin:jadwal_kegiatan_jadwalkegiatan_changelist"),
                    },
                  ],
              },
                {
                "title":"jadwal kunjungan",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"jadwal",
                        "icon": "schedule",
                        "link": reverse_lazy("admin:jadwal_kunjungan_jadwalkunjungan_changelist"),
                    },
                  ],
              },
                {
                "title":"kotak saran",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"saran",
                        "icon": "mark_unread_chat_alt",
                        "link": reverse_lazy("admin:kotaksaran_kotaksaran_changelist"),
                    },
                  ],
              },
                {
                "title":"sarana prasarana",
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title":"list sarpras",
                        "icon": "warehouse",
                        "link": reverse_lazy("admin:sarpras_sarpras_changelist"),
                    },
                  ],
              },
              ],
    },
    
    
}
