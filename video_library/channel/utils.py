from .models import Channel


def get_or_create_channel(name, channel_id):
    channel, created_channel = Channel.objects.get_or_create(name=name, channel_id=channel_id)
    if channel:
        return channel
    return created_channel
