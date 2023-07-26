from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from . import models
from .serializers import ArticleSerializer, ReaderSerializer
# Create your views here.
def articlesView(request):
    articles = models.Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)
    
    