from os import getcwd
from django.views import View
from django.http import FileResponse,JsonResponse

class File(View):
    def get(self,req):
        return FileResponse(open(getcwd()+'/cralwer/img/1234.png','rb'))
        
    def post(self,req):
        return JsonResponse({'message':'보낼 생각 없음'})