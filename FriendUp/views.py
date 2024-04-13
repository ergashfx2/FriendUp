from django.http import HttpResponse
from django.shortcuts import render, redirect


def home_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('posts:main-post-view')
    else:
        return redirect('profiles:login')