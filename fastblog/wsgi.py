#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fastblog.settings")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fastblog.settings")

from django.core.wsgi import get_wsgi_application
#jjj
from dj_static import Cling
#jjj
application = Cling( get_wsgi_application() )
