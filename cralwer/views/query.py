import json
from wsgiref.simple_server import WSGIRequestHandler
from django.views import View
from django.http import JsonResponse

from cralwer.controller.corona_controller import corona_api
from cralwer.controller.sports_schedule import get_url
from cralwer.controller.kbo_history import winning_rate
from cralwer.controller.contents import *


class Query(View):
    def get(self, req: WSGIRequestHandler):
        q = json.loads(req.GET.get('message'))[1:]
        response_data = {'data':'잘못된 입력'}
        
        if q[0] in ['야구','농구','해외야구','축구','해외축구','배구']:
            a = get_url(q[0])
            if q.__len__() > 1 and q[1] =='야구승률':
                team1 = q[2]
                team2 = q[3]
                response_data['data'] = winning_rate(team1,team2)
            else:
                response_data['data'] = a
        elif q[0] == '코로나':
            response_data['data'] = corona_api(q[1:])
        elif q[0] == '웹툰':
            if q[1] == '남자':
                response_data['data'] = naver_webtoon_male(q[2])
            elif q[1] =='여자':
                response_data['data'] = naver_webtoon_female(q[2])
            else:
                response_data['data'] = n2(q[2])
        elif q[0] == '차트':
            if q[1] == '멜론':
                response_data['data'] = get_melon_chart()
            elif q[1] == '벅스':
                response_data['data'] = bugs_chart()
        elif (q[0] == '도서') or(q[0] == '베스트셀러'):
            if q[1] == '20대':
                response_data['data'] = book_20()
            elif q[1] == '30대':
                response_data['data'] = book_30()
        elif (q[0] == '인기검색어') or(q[0] == '구글트렌드'):
                response_data['data'] = googledaily()
        
        return JsonResponse(response_data)
