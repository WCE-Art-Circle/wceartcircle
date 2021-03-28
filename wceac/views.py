from django.shortcuts import render
from django.views import View
from team.models import member

def error_404(request, exception):
        message = {}
        message['error']='Error 404, Page not found.'
        return render(request,'error.html', message)

def error_500(request):
        message = {}
        message['error']='Error 500, Server error.'
        return render(request,'error.html', message)

def error_403(request, exception):
        message = {}
        message['error']='Error 403, Request forbidden.'
        return render(request,'error.html', message)

def error_400(request, exception):
        message = {}
        message['error']='Error 400, Invalid request.'
        return render(request,'error.html', message)

class landing(View):

    def get(self,request,template_name='landing.html'):
        active_members = member.objects.filter(valid=True)
        message={}
        message['member']=active_members
        return render(request,template_name,message)