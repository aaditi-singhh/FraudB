import os
import sys

# Ensure Python path is aware of the current project level
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings')
application = get_wsgi_application()

app = application
