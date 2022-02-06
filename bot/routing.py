from django.urls import re_path
from bot.websocket import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/chatroom/$', consumers.ChatConsumer.as_asgi()),
]