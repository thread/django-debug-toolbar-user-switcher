SECRET_KEY = 'very-secret-value'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes', # needed by django.auth
    'django.contrib.sessions',
    'debug_toolbar',
    'debug_toolbar_user_switcher',
]

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'tests.urls'

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': (),
        'OPTIONS': {
            'debug': True,
            'builtins': [],
        },
    },
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar_user_switcher.panels.UserPanel',
)

DEBUG_TOOLBAR_USER_DEBUG = True
