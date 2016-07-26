from scaffold.settings import *

SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 2592000 #30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True

SECURE_REDIRECT_EXEMPT = [
    # App Engine doesn't use HTTPS internally, so the /_ah/.* URLs need to be exempt.
    # Django compares these to request.path.lstrip("/"), hence the lack of preceding /
    r"^_ah/"
]

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False

# Remove unsafe-inline from CSP_STYLE_SRC. It's there in default to allow
# Django error pages in DEBUG mode render necessary styles
if "'unsafe-inline'" in CSP_STYLE_SRC:
    CSP_STYLE_SRC = list(CSP_STYLE_SRC)
    CSP_STYLE_SRC.remove("'unsafe-inline'")
    CSP_STYLE_SRC = tuple(CSP_STYLE_SRC)

# Add the cached template loader for the Django template system (not for Jinja)
for template in TEMPLATES:
    if (
        template['BACKEND'] == 'django.template.backends.django.DjangoTemplates' and
        not template['OPTIONS'].get('loaders')
    ):
        # If and only if 'APP_DIRS' was True, include the app_directories loader as a sub-loader
        # of the cached loader
        app_dirs = template.get('APP_DIRS')
        sub_loaders = ['django.template.loaders.filesystem.Loader']
        if app_dirs:
            sub_loaders.append('django.template.loaders.app_directories.Loader')
        if app_dirs is not None:
            del template['APP_DIRS']

        template['OPTIONS']['loaders'] = [('django.template.loaders.cached.Loader', sub_loaders)]
