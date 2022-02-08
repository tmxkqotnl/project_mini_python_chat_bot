from django.shortcuts import render,redirect
from django.views import View
from django.core.handlers.asgi import ASGIRequest
from django.utils import timezone
from cralwer_child.models.searched import ChatContent
from uuid import uuid4,UUID

from cralwer_child.models.user import Client


class ChatRoom(View):
    def get(self, req: ASGIRequest):
        if not "user_id" in req.session or not "user_pk" in req.session:
            return redirect('login')

        return render(
            req,
            "bot/chatroom.html",
            {
                "user_id": req.session["user_id"],
                "user_pk": req.session["user_pk"],
            },
        )

    def post(self, req: ASGIRequest):
        if not "user_id" in req.session or not "user_pk" in req.session:
            return redirect('login')
        
        message = req.POST.get("message")
        create_dt = timezone.localtime()
        
        if message:
            ChatContent.objects.create(
                id=uuid4(),
                user_pk=Client.objects.get(id=UUID(req.session['user_pk'])),
                content=message,
                create_dt=create_dt,
                static_url=None,
            )

        return render(req,'bot/chatroom.html',{'user':req.session['user_id']})
