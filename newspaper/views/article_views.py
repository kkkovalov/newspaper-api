from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

# rest_framework packages
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions as rest_exceptions
from rest_framework_simplejwt.tokens import RefreshToken

# local packages
from newspaper import models, forms
from newspaper.serializers import ArticleSerializer, UserSerializer
# Article views
@api_view(['GET'])
def articlesView(request):
    articles = models.Article.objects.all()
    articles_serializer = ArticleSerializer(articles, many=True)
    return Response(articles_serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

# Topic views

@api_view(['GET'])
def topicView(request):
    pass

# User views

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