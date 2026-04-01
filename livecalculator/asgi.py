
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livecalculator.settings')
django.setup()


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    
    
})