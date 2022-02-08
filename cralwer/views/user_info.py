from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from cralwer.models.searched import Searched
from django.core.handlers.asgi import ASGIRequest
from django.core import serializers


class UserInfo(View):
    def get(self, req: ASGIRequest):
        if not "user_id" in req.session or not "user_pk" in req.session:
            return redirect("chat")

        msgs = serializers.serialize('json',ChatContent.objects.all().order_by("-create_dt"))

        res = {
            "user_id": req.session["user_id"],
            "user_pk": req.session["user_pk"],
            "message": msgs,
        }
        return JsonResponse(res)

    def post(self, req: ASGIRequest):
        if not "user_id" in req.session or not "user_pk" in req.session:
            return redirect("chat")

        return JsonResponse({"message": "no post response"})

