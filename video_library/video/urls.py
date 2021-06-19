from django.urls import path

from .views import VideoView, VideoSearchView, VideoDashboardView

urlpatterns = [
    path('', VideoView.as_view()),
    path('search/', VideoSearchView.as_view()),
    path('search_q/', VideoDashboardView.as_view())
]
