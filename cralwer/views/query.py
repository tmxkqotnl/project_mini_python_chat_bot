from wsgiref.simple_server import WSGIRequestHandler
from django.views import View
from django.http import JsonResponse

from cralwer.controller.corona_controller import corona_api

class Query(View):
    def get(self, req: WSGIRequestHandler):
        
        response_data = {}
        
        ## 여기에 여러분의 함수를 집어넣어 보세요.
        ## 그리고 다음 객체에 값을 집어넣어봐요
            
        response_data['YEAH'] = corona_api()
        
        return JsonResponse(response_data)