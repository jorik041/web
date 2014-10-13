"""
WSGI config for ask_pupkin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
#def application(environ, start_response):
 #   #start_response('200 OK', [('Content-Type','text/html')])
  #  return ["Hello World"]

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask_pupkin.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
