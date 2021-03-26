from django.shortcuts import render
from django.views import View
from .models import blog
# Create your views here.

class publish(View):
    message={}
    try:
        author_name=request.POST.get('author_name')
        author_artC=request.POST.get('author_artC')
        published_date=request.POST.get('published_date')
        title=request.POST.get('title')
        content=request.POST.get('content')
        blog_entry=blog(author_name=author_name,author_artC=author_artC,published_date=published_date,title=title,content=content)
        blog_entry.save()
    except:
        message['error']='Something went wrong. Please try again.'
