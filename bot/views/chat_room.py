from django.shortcuts import render
from django.views import View
    
class ChatRoom(View):
    def get(self,req):
        user_name = req.session.get('user')
        if not user_name:
            return render(req,'bot/index.html')
        
        return render(req,'bot/chatroom.html',{'user_name':user_name})
    
    def post(self,req):
        return render(req,'bot/chatroom.html')