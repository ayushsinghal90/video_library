from rest_framework.serializers import ModelSerializer

from .models import Video
from video_library.channel.serializers import ChannelSerializer


class VideoSerializer(ModelSerializer):
    channel = ChannelSerializer()

    class Meta:
        model = Video
        fields = ('id', 'video_id', 'channel', 'title', 'description', 'thumbnail', 'publishing_on')
