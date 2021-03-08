from django.shortcuts import render
from django.views import View

class landing(View):

    def get(self,request,template_name='landing.html'):
        return render(request,template_name)