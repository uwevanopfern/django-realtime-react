# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
from django.urls import path 

from . import consumers

websocket_urlpatterns = [
  path('ws/notes', consumers.NoteConsumer)
]
