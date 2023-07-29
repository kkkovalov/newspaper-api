from .user_views import *
from .article_views import *
from .creator_views import *
from .topic_views import *

from django.shortcuts import render
from django.http import JsonResponse

def homeView(request):
    return render(request, 'newspaper/home.html')

def badRequest(request):
    return JsonResponse({'detail': 'Bad Request'}, status=403)