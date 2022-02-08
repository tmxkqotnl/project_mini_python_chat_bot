from typing import Optional
from django.shortcuts import redirect, render
from django.views import View

from django.core.handlers.asgi import ASGIRequest

from cralwer.models.user import User
from django.contrib.auth.hashers import make_password
from uuid import uuid4

class Login(View): # class view
    def get(self,req:ASGIRequest):
        if 'user_token' in req.session:
            return redirect('chat')
        
        return render(req,'cralwer/index.html')
    
    def post(self,req:ASGIRequest):
        user_id = req.POST.get('user_id')
        user_pw = req.POST.get('password')
        checkbox = True if req.POST.get('create') else False
        
        msg = {'message':'아이디 또는 비밀번호를 확인해주세요.'}
        
        user_info:Optional[Client] = None
        if checkbox:
            user_info = Client.objects.filter(user_id=user_id).first()
            if user_info:
                return render(req,'cralwer/index.html',msg)
            else:
                user_info = Client.objects.create(id=uuid4(),user_id=user_id,password=make_password(user_pw))
        else:
            user_info = Client.objects.filter(user_id=user_id,password=make_password(user_pw)).first()
            if not user_info:
                return render(req,'cralwer/index.html',msg)
        
        
        return redirect('chat')