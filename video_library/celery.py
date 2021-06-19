from __future__ import absolute_import

import logging
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_videos.settings')
app = Celery('youtube_videos')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

LOG = logging.getLogger(__name__)


@app.task(bind=True)
def debug_task(self):
    LOG.info('Request: {0!r}'.format(self.request))
