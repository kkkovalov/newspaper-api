from .user_views import *
from .article_views import *
from django.shortcuts import render

def homeView(request):
    return render(request, 'newspaper/home.html')

