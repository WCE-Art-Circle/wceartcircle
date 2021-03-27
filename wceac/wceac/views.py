from django.shortcuts import render
from django.views import View
from team.models import member
class landing(View):

    def get(self,request,template_name='landing.html'):
        active_members = member.objects.filter(valid=True)
        message={}
        message['member']=active_members
        return render(request,template_name,message)