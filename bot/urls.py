from django.urls import path 
from bot.views import login,chat_room

urlpatterns = [ 
    path('' , login.Login.as_view() , name='login'),
    path('chatroom',chat_room.ChatRoom.as_view(),name='chat')
]