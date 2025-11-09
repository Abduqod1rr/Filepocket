"""
WSGI config for FilePocket project.
"""

import os
import sys
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the project directory to Python path
# This ensures FilePocket module can be found
sys.path.insert(0, str(BASE_DIR))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FilePocket.settings')

application = get_wsgi_application()