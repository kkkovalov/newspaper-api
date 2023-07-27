from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from . import models
from .serializers import ArticleSerializer, UserSerializer
from django.core import exceptions


# Create your views here.

def homeView(request):
    return render(request, 'newspaper/home.html')

def articlesView(request):
    articles = models.Article.objects.all()
    articles_serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(articles_serializer.data, safe=False)
    
def singleArticleView(request, id):
    if request.method == "GET":
        try:
            article = models.Article.objects.get(id=id)
        except:
            return exceptions.ObjectDoesNotExist
        article_serializer = ArticleSerializer(article)
        return JsonResponse(article_serializer.data)
    else:
        return exceptions.BadRequest

def articlesByTopicView(request, topic):
    pass

def creatorView(request, username):
    if request.method == 'GET':
        try:
            user = models.User.objects.get(username=username)
            articles = models.Article.objects.filter(creator=user)
        except:
            return exceptions.ObjectDoesNotExist
        article_serializer = ArticleSerializer(articles, many=True)
        user_serializer = UserSerializer(user)
        json_context = {
            'user': user_serializer.data,
            'articles': article_serializer.data,
        }
        return JsonResponse(json_context, safe=False)
        
        # return JsonResponse(user_serializer.data)
    else:
        return exceptions.BadRequest