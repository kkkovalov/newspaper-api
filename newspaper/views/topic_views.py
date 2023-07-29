from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.text import slugify

# rest_framework packages
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions as rest_exceptions

# local packages
from newspaper.models import Topic
from newspaper.serializers import TopicSerializer
from newspaper.views.creator_views import is_creator
    
class TopicView(APIView):
    
    def get(self, request, format=None):
        try:
            topics_list = Topic.objects.all()
        except:
            raise rest_exceptions.NotFound
        serializer = TopicSerializer(topics_list, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, format=None):
        if request.user.is_authenticated:
            if is_creator(request.user):
                return Response({'detail': 'post request response'}, status=200)
            else:
                raise rest_exceptions.PermissionDenied
        else:
            raise rest_exceptions.AuthenticationFailed
    
    def put(self, request, format=None):
        return Response({'detail': 'put request response'}, status=200)
    
    def delete(self, request, format=None):
        return Response({'detail': 'delete request response'}, status=200)

