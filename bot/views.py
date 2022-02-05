from django.shortcuts import redirect, render
from django.views import View
from bot.models import client

class Login(View): # class view
    def get(self,req):
        if req.session.get('user'):
            return redirect('chat')
        
        return render(req,'bot/index.html')
    
    def post(self,req):
        user_id = req.POST.get('user_id')
        user_pw = req.POST.get('password')
        checkbox = True if req.POST.get('create') else False
        
        user_info = client.objects.filter(user_id=user_id,password=user_pw).first()
        msg = {'message':'아이디 또는 비밀번호를 확인해주세요.'}
        if checkbox:
            user_info = client.objects.filter(user_id=user_id).first()
            if user_info:
                return render(req,'bot/index.html',msg)
            else:
                client.objects.create(user_id=user_id,password=user_pw,name='TEST')
        else:
            user_info = client.objects.filter(user_id=user_id,password=user_pw).first()
            if not user_info:
                return render(req,'bot/index.html',msg)
        
        req.session['user'] = user_id
        return redirect('chat')
    
class ChatRoom(View):
    def get(self,req):
        user_name = req.session.get('user')
        if not user_name:
            return render(req,'bot/index.html')
        
        return render(req,'bot/chatroom.html',{'user_name':user_name})
    
    def post(self,req):
        return render(req,'bot/chatroom.html')