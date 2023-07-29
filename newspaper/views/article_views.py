from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

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
    if request.method == "GET":
        try:
            articles = models.Article.objects.all()
        except:
            raise rest_exceptions.APIException
        articles_serializer = ArticleSerializer(articles, many=True)
        return Response(articles_serializer.data, status=200)
    else:
        raise rest_exceptions.MethodNotAllowed
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def singleArticleView(request, slug_name):
    
    if request.method == "GET":
        try:
            article = models.Article.objects.get(slug_name=slug_name)
        except:
            raise rest_exceptions.NotFound
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data, status=200)
    else:
        raise rest_exceptions.MethodNotAllowed

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