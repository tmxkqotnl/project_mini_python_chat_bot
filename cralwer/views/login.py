from django.utils.timezone import localdate
from typing import Optional
from django.shortcuts import redirect, render
from django.views import View

from django.core.handlers.asgi import ASGIRequest

from cralwer.models.user import User
from cralwer.models.token import Token
from django.contrib.auth.hashers import make_password,check_password
from uuid import uuid4,UUID

class Login(View): # class view
    def get(self,req:ASGIRequest):
        return render(req,'cralwer/index.html')
    
    def post(self,req:ASGIRequest):
        user_id = req.POST.get('user_id') # 암호화 해야함
        user_pw = req.POST.get('password')
        checkbox = req.POST.get('sex')
        
        msg = {'message':'아이디 또는 비밀번호를 확인해주세요.'}
        user_info:Optional[User] = User.objects.filter(user_id=user_id).first()
        
        if isinstance(user_info,User):
            if not check_password(user_pw,user_info.password): 
                return redirect('/',req,msg)    
            
            token_uuid = uuid4()
            user_token:Token = Token.objects.get(user_pk = user_info.id)
            user_token.token = token_uuid
            user_token.save()
            req.session['user_token'] = str(token_uuid)
        else:
            token_uuid = uuid4()
            user_info = User.objects.create(id=uuid4(),user_id=user_id,password=make_password(user_pw),sex=checkbox)
            Token.objects.create(id=uuid4(),user_pk = user_info,token=token_uuid)
            req.session['user_token'] = str(token_uuid)
            
        return redirect('chat')