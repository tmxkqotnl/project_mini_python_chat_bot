from wsgiref.simple_server import WSGIRequestHandler
from django.views import View
from django.http import JsonResponse

from cralwer.controller.corona_controller import corona_api

class Query(View):
    def get(self, req: WSGIRequestHandler):
        
        q = req.GET.get('message')
        corona_api(queries=q)
        
        return JsonResponse({'data':corona_api()})