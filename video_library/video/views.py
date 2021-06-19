import logging

from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import SearchVector

from .constants import SORT_MAPPER, PUBLISHED_DATE
from .models import Video
from .serializers import VideoSerializer
from video_library.utils.commons import get_api_error_response
from video_library.utils.api_response_messages import ERROR_MESSAGE, SERVER_ERROR

LOG = logging.getLogger(__name__)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class VideoView(APIView, LargeResultsSetPagination):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        """
        Fetch all video details from DataBase
        :param request:
            page:int = page_number
        :return: Return list of video details in order of published_on in paginated format with next page link.
        """
        try:
            videos = Video.objects.all().order_by('publishing_on')
            videos = self.paginate_queryset(videos, request, view=self)
            data = VideoSerializer(videos, many=True).data
            data = self.get_paginated_response(data)
            return data
        except Exception as e:
            LOG.error(e.__str__())
            return get_api_error_response(status=500, message=ERROR_MESSAGE[SERVER_ERROR])


class VideoSearchView(APIView, LargeResultsSetPagination):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        """
        Fetch video details for search_text given in the api in order of published_on.
        :param request:
            search_text:str = search text
            page:int = page_number
        :return: Return list of video details in order of published_on in paginated format with next page link.
        """
        try:
            search_text = request.data.get('search_text', None)
            if search_text:
                videos = Video.objects.annotate(search=SearchVector('title', 'description'),).\
                    filter(search=search_text).select_related('channel').order_by('publishing_on')
            else:
                videos = Video.objects.all().order_by('publishing_on')
            videos = self.paginate_queryset(videos, request, view=self)
            data = VideoSerializer(videos, many=True).data
            data = self.get_paginated_response(data)
            return data
        except Exception as e:
            LOG.error(e.__str__())
            return get_api_error_response(status=500, message=ERROR_MESSAGE[SERVER_ERROR])


class VideoDashboardView(APIView, LargeResultsSetPagination):
    pagination_class = LargeResultsSetPagination

    def get(self, request):
        """
        Fetch video details for search_text given in the api in order of published_on.
        particular order.
        :param request:
            search_q:str = search text
            sort:str = sort order ['title', 'description', 'publishing_on'] prefix '-' for reverse order
            page:int = page_number
        :return: RReturn list of video details in order of published_on in paginated format with next page link.
        """
        try:
            search_text = request.data.get('search_q', None)
            sort_term = sort = request.data.get('sort', PUBLISHED_DATE)
            asc_order = True
            sort_field = PUBLISHED_DATE
            if sort[0] == '-':
                sort_term = sort[1:]
                asc_order = False
            if SORT_MAPPER.get(sort_term):
                sort_field = SORT_MAPPER.get(sort_term)
                sort_field = sort_field if asc_order else '-' + sort_field

            if search_text:
                videos = Video.objects.annotate(search=SearchVector('title', 'description'), ). \
                    filter(search=search_text).select_related('channel').order_by(sort_field)
            else:
                videos = Video.objects.all()
            videos = self.paginate_queryset(videos, request, view=self)
            data = VideoSerializer(videos, many=True).data
            data = self.get_paginated_response(data)
            return data
        except Exception as e:
            LOG.error(e.__str__())
            return get_api_error_response(status=500, message=ERROR_MESSAGE[SERVER_ERROR])