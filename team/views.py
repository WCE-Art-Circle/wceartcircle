from django.shortcuts import render
from .models import member
from django.views import View
# Create your views here.

class MemberRegistration(View):

    def get(self,request,template_name="register-as-member.html"):
        return render(request,template_name)

    def post(self,request,template_name="register-as-member.html"):
        message={}
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            board = request.POST.get('board')
            position = request.POST.get('position')
            team = request.POST.get('team')
            photo = request.POST.get('photo')
            photo = "https://drive.google.com/thumbnail?id=" + photo[32:65]
            description = request.POST.get('description')
            insta = request.POST.get('insta')
            artwork = request.POST.get('artwork')
            artworklink = request.POST.get('artworklink')
            Member = member(first_name=first_name,last_name=last_name,board=board,position=position,team=team,photo=photo,description=description,insta=insta,artwork=artwork,artworklink=artworklink)
            Member.save()
            message['error']='Registered Successfully.'
            print('DONE')
        except:
            message['error']='Something went wrong, try again.'
        return render(request,template_name,message)
        







