from django.urls import path 
from cralwer.views import login,chat_room, files

urlpatterns = [ 
    path('' , login.Login.as_view() , name='login'),
    path('chatroom',chat_room.ChatRoom.as_view(),name='chat'),
    path('img',files.File.as_view(),name='info'),
]