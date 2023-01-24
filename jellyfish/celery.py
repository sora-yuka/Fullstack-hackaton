import os
import django
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jellyfish.settings')
django.setup()
app = Celery('jellyfish')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



# [program:celery]
# command=/home/dcabatar/fullstack/venv/bin/celery -A jellyfish worker --loglevel=INFO
# directory=/home/dcabatar/fullstack/
# user=www-data
# autostart=true
# autorestart=true
# startsecs=0
# stdout_logfile=/home/dcabatar/fullstack/logs/celeryd.log
# redirect_stderr=true