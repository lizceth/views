from django.http import HttpResponse
from django.views.generic import view

class LoginView(view):
    def get(self,request,*arg,**kwarg):
        return HttpResponse('login view')

