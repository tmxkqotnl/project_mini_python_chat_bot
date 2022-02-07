from django.views import View
from django.http import JsonResponse

class UserInfo(View):
    def get(self,req):
        if not 'user_id' in req.session or not 'user_pk' in req.session:
            return {'message':'no session info found'}
        
        return JsonResponse({'message':'Ok','user_id':req.session['user_id'],'user_pk':req.session['user_pk']})
    
    def post(self,req):
        return JsonResponse({'message':"no post response"}) 