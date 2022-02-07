from django.shortcuts import render
from django.views import View
from django.core.handlers.asgi import ASGIRequest
from json import loads
    
class ChatRoom(View):
    def get(self,req:ASGIRequest):
        if not 'user_id' in req.session or not 'user_pk' in req.session:
            return render(req,'bot/index.html')
        
        return render(req,'bot/chatroom.html',{'user_id':req.session['user_id'],'user_pk':req.session['user_pk']})
    
    def post(self,req:ASGIRequest):
        return render(req,'bot/chatroom.html')