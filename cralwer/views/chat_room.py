from json import loads
from django.shortcuts import render
from django.views import View
from django.core.handlers.asgi import ASGIRequest
from cralwer.const import CATEGORIES, CRAWLING_START

from cralwer.models.searched import Searched
from cralwer.models.token import Token
from cralwer.models.query import Query

from uuid import uuid4

class ChatRoom(View):
    def get(self, req: ASGIRequest):
        return render(
            req,
            "cralwer/chatroom.html",
        )

    def post(self, req: ASGIRequest):
        message = loads(req.POST.get("message"))
        user_token = Token.objects.get(token=req.session['user_token'])
        
        Searched.objects.create(
                id=uuid4(),
                input_text=" ".join(message),
                user_pk=user_token.user_pk
        )
        
        response_data = {}
        if message[0] == CRAWLING_START and message.__len__()>1:
            categories = message[1:]
            
            for i in range(len(categories),len(CATEGORIES)):
                categories = categories + [None]
                
            Query.objects.create(
                id = uuid4(),
                user_pk = user_token.user_pk,
                large=categories[0],
                medium=categories[1],
                small=categories[2]
            )
        
        return render(req,'cralwer/chatroom.html',response_data)
