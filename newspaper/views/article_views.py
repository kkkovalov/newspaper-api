from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.text import slugify

# rest_framework packages
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions as rest_exceptions

# local packages
from newspaper import models, forms
from newspaper.serializers import ArticleSerializer


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
