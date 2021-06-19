from .models import Keys
from .constants import YOUTUBE


def get_keys_for_youtube():
    api_keys = Keys.objects.filter(type=YOUTUBE, status=Keys.SUCCESS).order_by('created_at')
    return api_keys
