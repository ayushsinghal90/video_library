import logging
import requests

from django.conf import settings
from .constants import YOUTUBE_SEARCH_URL

LOG = logging.getLogger(__name__)


def send(key, published_after):
    params = {
        'part': "snippet",
        'q': settings.SEARCH_KEYWORD,
        'type': "video",
        'key': key,
        'publishedAfter': published_after,
        'maxResults': settings.MAX_RESULTS
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params)
    response = response.json()
    LOG.info(response)
    return response
