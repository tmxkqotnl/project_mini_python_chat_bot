from http.client import HTTPResponse
from django.shortcuts import redirect

class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, req):
        
        response = self.get_response(request)
        
        return response
    def process_request(self,req):
        print(req.path.__len__())
        if 'user_token' in req.session and req.path.__len__() == 1:
            return None
        
        return redirect('/')