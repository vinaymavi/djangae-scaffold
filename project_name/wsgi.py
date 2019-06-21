"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from {{ project_name }}.boot import fix_path

# This is a copy from djangae.environment, but we can't import that until we've called fix_path()
def is_development_environment():
    return 'SERVER_SOFTWARE' not in os.environ or os.environ['SERVER_SOFTWARE'].startswith("Development")

fix_path(include_dev_libs_path=is_development_environment())

from django.core.wsgi import get_wsgi_application
from djangae.environment import is_production_environment
from djangae.wsgi import DjangaeApplication

settings = "{{ project_name }}.settings_live" if is_production_environment() else "{{ project_name }}.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)



application = DjangaeApplication(get_wsgi_application())
