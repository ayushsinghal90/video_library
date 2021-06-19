import logging
from datetime import datetime, timedelta

from celery import shared_task
from video_library.video.models import Video
from video_library.keys.models import Keys
from video_library.keys.utils import get_keys_for_youtube
from video_library.channel.utils import get_or_create_channel
from video_library.core import youtube_api

LOG = logging.getLogger(__name__)

SCHEDULED_QUERY_TIME = 700


@shared_task
def youtube_sync_engine():
    """
    Task to fetch latest youtube videos using youtube api periodically at
    particular intervals and save then in our database.
    :return:
    """
    published_after = datetime.now()-timedelta(minutes=SCHEDULED_QUERY_TIME)
    published_after = "{}T{}Z".format(str(published_after.date()), str(published_after.time())[:8])
    api_keys = get_keys_for_youtube()
    for api_key in api_keys:
        response = youtube_api.send(api_key.key, published_after)
        if response.get('error'):
            api_key.status = Keys.FAILED
            api_key.save()
            LOG.error("Valid API Key not Present")
        else:
            response = response.get('items', None)
            for video in response:
                video_id = video['id']['videoId']

                video_details = video['snippet']
                channel_id = video_details['channelId']
                title = video_details['title']
                description = video_details['description']
                channel_name = video_details['channelTitle']
                publishing_date = video_details['publishTime']
                thumbnail_url = video_details['thumbnails']["default"]["url"]

                channel = get_or_create_channel(channel_name, channel_id)

                _, _ = Video.objects.get_or_create(title=title, description=description, thumbnail=thumbnail_url,
                                                   publishing_on=publishing_date, channel_id=channel.id,
                                                   video_id=video_id)
                LOG.info("New Video saved: {}".format(video_id))
            break
