import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fengwuu_test.settings')

app = Celery('fengwuu')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
