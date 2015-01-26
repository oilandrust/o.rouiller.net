from orouiller.settings.common import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
)
