import os
import sys

# Make sure the project root is in the python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings')
app = get_wsgi_application()
