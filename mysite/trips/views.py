#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime
# from django.http import HttpResponse
from django.shortcuts import render
from trips.models import Post

# Create your views here.
def hello_world_old(request):
    output = """
        <!DOCTYPE html>
        <html>
            <head>
            </head>
            <body>
                Hello World! <em style="color:LightSeaGreen;">{current_time}</em>
            </body>
    """.format(current_time=datetime.now())
    return HttpResponse(output)

def hello_world(request):
    return render(request,
                  'hello_world.html',
                 {'current_time': datetime.now()})

def home(request):
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post':post})