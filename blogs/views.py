from django.shortcuts import render
from django.views import View
from .models import blog
# Create your views here.

#class login(View):
    

class publish(View):
    def get(self,request,template_name="addBlog.html"):
        return render(request,template_name)

    def post(self,request,template_name="addBlog.html"):
        message={}
        try:
            author_name=request.POST.get('author_name')
            author_artC=request.POST.get('author_artC')
            published_date=request.POST.get('published_date')
            title=request.POST.get('title')
            content=request.POST.get('content')
            blog_entry=blog(author_name=author_name,author_artC=author_artC,published_date=published_date,title=title,content=content)
            blog_entry.save()
            message['error']='Blog published successfully.'
        except:
            message['error']='Something went wrong. Please try again.'
        return render(request,template_name,message)
