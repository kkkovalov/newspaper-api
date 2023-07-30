# rest_framework packages
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# local packages
from newspaper import models, forms
from newspaper.serializers import ArticleSerializer


# Article views

class AritcleView(APIView):
    """
    Article view class that handles all requests and configures authentication
    """
    def get(self, request, format=None):
        pass
    def post(self, request, format=None):
        pass
    def put(self, request, format=None):
        pass
    def delete(self, request, format=None):
        pass

@api_view(['GET'])
def articlesView(request):
    if request.method == "GET":
        try:
            articles = models.Article.objects.all()
        except:
            raise exceptions.APIException
        articles_serializer = ArticleSerializer(articles, many=True)
        return Response(articles_serializer.data, status=200)
    else:
        raise exceptions.MethodNotAllowed
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def singleArticleView(request, slug_name):
    
    if request.method == "GET":
        try:
            article = models.Article.objects.get(slug_name=slug_name)
        except:
            raise exceptions.NotFound
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data, status=200)
    else:
        raise exceptions.MethodNotAllowed
