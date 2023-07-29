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
from rest_framework_simplejwt.tokens import RefreshToken

# local packages
from newspaper import models, forms
from newspaper.serializers import ArticleSerializer, UserSerializer

def is_creator(user):
    return user.groups.filter(name="Creator").exists()

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@user_passes_test(is_creator, login_url='bad-request')
def newArticleView(request):
    pass

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@user_passes_test(is_creator, login_url='bad-request')
def editArticleView(request):
    pass


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@user_passes_test(is_creator, login_url='bad-request')
def newTopicView(request):
    pass

