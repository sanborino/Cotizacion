"""
WSGI config for Cotizacion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cotizacion.settings")

application = get_wsgi_application()



# sys.path = ['C:\proyecto\www', 'C:\Python27\Lib\site-packages'] + sys.path

# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# import django.core.handlers.wsgi

# application = django.core.handlers.wsgi.WSGIHandler()