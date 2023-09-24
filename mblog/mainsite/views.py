from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
import logging

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            return render(request, 'post.html', locals())

    except Exception as e:
        logging.warning(e)
        return redirect('/')
