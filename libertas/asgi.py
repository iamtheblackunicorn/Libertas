# Libertas by Alexander Abraham, "The Black Unicorn".
# Licensed under the MIT license.
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libertas.settings')
application = get_asgi_application()
