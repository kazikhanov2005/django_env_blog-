from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    posts = Post.objects.all()
    context = {
        'title': 'Home',
        'posts': posts,
    }
    c = 0
    current_user = request.user

    if current_user.is_superuser and c == 0:
        c += 1
        messages.success(request, 'Вы являетесь Администратором сайта!')

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})