from __future__ import absolute_import

import logging
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_library.settings')
app = Celery('video_library')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

LOG = logging.getLogger(__name__)

app.conf.beat_schedule = {
    'youtube_sync_engine': {
        'task': 'video_library.scheduled_task.tasks.youtube_sync_engine',
        'schedule': crontab(minute='*/1')  # execute every minute
    }
}


@app.task(bind=True)
def debug_task(self):
    LOG.info('Request: {0!r}'.format(self.request))
