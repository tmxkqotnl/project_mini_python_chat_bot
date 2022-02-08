from django.shortcuts import render
from django.views import View
from django.core.handlers.asgi import ASGIRequest
from django.utils import timezone
from uuid import uuid4,UUID
from cralwer.const import CRAWLING_START
from cralwer.models.searched import Searched

from cralwer.models.user import User
from cralwer.models.token import Token


class ChatRoom(View):
    def get(self, req: ASGIRequest):
        return render(
            req,
            "cralwer/chatroom.html",
        )

    def post(self, req: ASGIRequest):
        message = req.POST.get("message")
        user_token = Token.objects.get(token=req.session['user_token'])
        
        create_dt = timezone.localtime()
        
        # if message[0] == CRAWLING_START:
        
        Searched.objects.create(
                id=uuid4(),
                input_text=" ".join(message),
                user_pk=user_token.user_pk
        )
        

        return render(req,'cralwer/chatroom.html')
