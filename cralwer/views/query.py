import json
from wsgiref.simple_server import WSGIRequestHandler
from django.views import View
from django.http import JsonResponse
import json

from cralwer.controller.corona_controller import corona_api
from cralwer.controller.sports_schedule import get_url
from cralwer.controller.kbo_history import winning_rate



class Query(View):
    def get(self, req: WSGIRequestHandler):
        q = json.loads(req.GET.get('message'))[1:]
        response_data = {'data':'잘못된 입력'}
        
        q = json.loads(req.GET.get('message'))
        a = 0
        if q[1] in ['야구','농구','해외야구','축구','해외축구','배구']:
            a = get_url(q[1])
            if q[1] =='야구승률':
                team1 = q[3]
                team2 = q[4]
                a = winning_rate(team1,team2)
                return JsonResponse({'data':a})
            else:
                return JsonResponse({'data':a})

        if q[0] == '코로나':
            response_data['data'] = corona_api(q[1:])
        
        return JsonResponse(response_data)
