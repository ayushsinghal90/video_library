from django.urls import path

from .views import KeysView

urlpatterns = [
    path('', KeysView.as_view())
]
