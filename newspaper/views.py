from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from . import models
from .serializers import ArticleSerializer, ReaderSerializer
from django.core import exceptions


# Create your views here.

def homeView(request):
    return render(request, 'newspaper/home.html')

def articlesView(request):
    articles = models.Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)
    
def singleArticleView(request, id):
    if request.method == "GET":
        try:
            article = models.Article.objects.get(id=id)
        except:
            return exceptions.ObjectDoesNotExist
    else:
        return exceptions.BadRequest

def articlesByTopicView(request, topic):
    pass

def creatorView(request, username):
    if request.method == 'POST':
        try:
            creator = models.Creator.objects.get(username=username)
        except:
            return exceptions.ObjectDoesNotExist            
    else:
        return exceptions.BadRequest