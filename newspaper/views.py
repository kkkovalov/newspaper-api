from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import exceptions

# rest_framework packages
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# local packages
from . import models
from .serializers import ArticleSerializer, UserSerializer

@api_view(['GET'])
def authenticateUser(request):
    user


# Create your views here.
def homeView(request):
    return render(request, 'newspaper/home.html')

@api_view(['GET'])
def articlesView(request):
    articles = models.Article.objects.all()
    articles_serializer = ArticleSerializer(articles, many=True)
    return Response(articles_serializer.data)
    
@api_view(['GET'])
def singleArticleView(request, id):
    if request.method == "GET":
        try:
            article = models.Article.objects.get(id=id)
        except:
            return exceptions.ObjectDoesNotExist
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data)
    else:
        return exceptions.BadRequest

def articlesByTopicView(request, topic):
    pass

@api_view(['GET', 'POST'])
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