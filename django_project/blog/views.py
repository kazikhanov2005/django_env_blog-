from .models import Post
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    posts = Post.objects.all()
    context = {
        'title': 'Home',
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})