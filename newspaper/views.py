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


# Create your views here.
def homeView(request):
    return render(request, 'newspaper/home.html')


