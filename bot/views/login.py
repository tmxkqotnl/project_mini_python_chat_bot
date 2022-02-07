from typing import Optional
from django.shortcuts import redirect, render
from django.views import View
from bot.models.client import Client
from uuid import uuid4

class Login(View): # class view
    def get(self,req):
        if 'user_id' in req.session and 'user_pk' in req.session:
            return redirect('chat')
        
        return render(req,'bot/index.html')
    
    def post(self,req):
        user_id = req.POST.get('user_id')
        user_pw = req.POST.get('password')
        checkbox = True if req.POST.get('create') else False
        
        msg = {'message':'아이디 또는 비밀번호를 확인해주세요.'}
        
        user_info:Optional[Client] = None
        if checkbox:
            user_info = Client.objects.filter(user_id=user_id).first()
            if user_info:
                return render(req,'bot/index.html',msg)
            else:
                user_info = Client.objects.create(id=uuid4(),user_id=user_id,password=user_pw)
        else:
            user_info = Client.objects.filter(user_id=user_id,password=user_pw).first()
            if not user_info:
                return render(req,'bot/index.html',msg)
        
        req.session['user_id'] = user_id
        req.session['user_pk'] = str(user_info.id)
        
        return redirect('chat')