import os
import sys

# Add the parent directory to the path so that python can find project_settings and other apps
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings')
application = get_wsgi_application()
app = application
