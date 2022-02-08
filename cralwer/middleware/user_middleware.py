from http.client import HTTPResponse
from django.shortcuts import redirect

class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, req):
        res = self.process_request(req)
        if not res:
            res = self.get_response(req)
        
        return res
    
    def process_request(self,req):
        cond = 'user_token' in req.session
        if req.path.__len__() != 1 and not cond:
            return redirect('/')
        elif req.path.__len__() == 1 and cond:
            return redirect('/chatroom')
        
        return None