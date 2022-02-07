from django.urls import path 
from bot.views import login,chat_room,user_info

urlpatterns = [ 
    path('' , login.Login.as_view() , name='login'),
    path('chatroom',chat_room.ChatRoom.as_view(),name='chat'),
    path('chatroom/user_info',user_info.UserInfo.as_view(),name='info')
]