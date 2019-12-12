"""
WSGI config for tesouro_direto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tesouro_direto.settings')

os.environ["SECRET_KEY"] ="19y$+lcx19z19o@y2s5$vw!6^!g@o7j-2#0ojyn_5#elgl)%v@"

application = get_wsgi_application()
