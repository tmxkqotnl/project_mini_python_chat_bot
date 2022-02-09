import json
from wsgiref.simple_server import WSGIRequestHandler
from django.views import View
from django.http import JsonResponse

from cralwer.controller.corona_controller import corona_api

class Query(View):
    def get(self, req: WSGIRequestHandler):
        q = json.loads(req.GET.get('message'))[1:]
        response_data = {'data':'잘못된 입력'}
        
        if q[0] == '코로나':
            response_data['data'] = corona_api(q[1:])
        
        return JsonResponse(response_data)