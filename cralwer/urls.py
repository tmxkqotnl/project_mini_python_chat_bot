from django.urls import path 
from cralwer.views import login,chat_room, files,query

urlpatterns = [ 
    path('' , login.Login.as_view() , name='login'),
    path('chatroom',chat_room.ChatRoom.as_view(),name='chat'),
    path('query',query.Query.as_view(),name='query'),
    path('img',files.File.as_view(),name='info'),
]