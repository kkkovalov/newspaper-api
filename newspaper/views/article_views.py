# rest_framework packages
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView


# local packages
from newspaper.models import Article
from newspaper.serializers import ArticleSerializer
from newspaper.views.creator_views import is_creator


# Article views

class AritcleView(APIView):
    """
    Article view class that handles all requests and configures authentication
    """
    def get(self, request, format=None):
        try:
            articles = Article.objects.all()
        except:
            raise exceptions.NotFound
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, format=None):
        if request.user.is_authenticated:
            if is_creator(request.user):
                serializer = ArticleSerializer(request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated
    def put(self, request, format=None):
        pass
    def delete(self, request, format=None):
        pass

    
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def singleArticleView(request, slug_name):
    
#     if request.method == "GET":
#         try:
#             article = models.Article.objects.get(slug_name=slug_name)
#         except:
#             raise exceptions.NotFound
#         article_serializer = ArticleSerializer(article)
#         return Response(article_serializer.data, status=200)
#     else:
#         raise exceptions.MethodNotAllowed
