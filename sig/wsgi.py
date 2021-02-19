"""
WSGI config for sig project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os 
import sys 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sig.settings')
sys.path.append('home/ubuntu/siggen')
sys.path.append('home/ubuntu/siggen/sig')


application = get_wsgi_application()
