import logging

from rest_framework.views import APIView
from .models import Keys
from video_library.utils.commons import get_api_error_response, get_api_success_response
from video_library.utils.api_response_messages import SUCCESS_MESSAGE, ERROR_MESSAGE, SUCCESS_CODE, KEY_CREATION_FAILED

LOG = logging.getLogger(__name__)


class KeysView(APIView):

    def post(self, request):
        try:
            type = request.data.get('type', None)
            key = request.data.get('key', None)
            _, _ = Keys.objects.get_or_create(type=type, key=key)
            return get_api_success_response(message=SUCCESS_MESSAGE[SUCCESS_CODE], status=201)
        except Exception as e:
            LOG.error("Key addition failed {}".format(e), exc_info=True)
            return get_api_error_response(status=500, message=ERROR_MESSAGE[KEY_CREATION_FAILED])