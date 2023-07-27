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
from . import models, forms
from .serializers import ArticleSerializer, UserSerializer


@api_view(['POST'])
def loginUser(request):
    if request.user.is_authenticated:
        return JsonResponse({'logged_in': True})
    
    elif request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = models.User.objects.get(username=username)
        except:
            return rest_exceptions.AuthenticationFailed
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'user found',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                })
        else:
            return JsonResponse({'message': 'user not found', }, status=404)
    else:
        return rest_exceptions.NotFound

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        
        if request.user.is_authenticated():
            return JsonResponse({'logged_in': True})
        
        # created a user based on user info (username, email, password1, password2)
        user = forms.ReaderCreationForm(request.POST)
        # if request.POST.get('email') == '':
        #     raise rest_exceptions.ValidationError
        if user.is_valid():
        
            user.save()
            return JsonResponse({'message': 'Successfuly added a user'})
        else:
            raise rest_exceptions.ValidationError
    else:
        raise rest_exceptions.APIException

# Create your views here.
def homeView(request):
    return render(request, 'newspaper/home.html')


# Article views
@api_view(['GET'])
def articlesView(request):
    articles = models.Article.objects.all()
    articles_serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(articles_serializer.data, safe=False)
    
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