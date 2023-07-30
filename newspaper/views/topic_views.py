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
        """
        Returns a list of JSON objects, if they exist in the database. No request body required.
        """
        try:
            topics_list = Topic.objects.all()
        except:
            raise rest_exceptions.NotFound
        serializer = TopicSerializer(topics_list, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, format=None):
        """
        Returns JSON confirmation of adding the topic to the database.
        """
        if request.user.is_authenticated:
            if is_creator(request.user):
                topic = TopicSerializer(data=request.data)
                topic.is_valid(raise_exception=True)
                topic.save()
                return Response(topic.data, status=200)
            else:
                raise rest_exceptions.PermissionDenied
        else:
            raise rest_exceptions.AuthenticationFailed
    
    def put(self, request, format=None):
        """
        Takes JSON object with keys (name, description). Returns updated object.
        """
        return Response({'detail': 'put request response'}, status=200)
    
    def delete(self, request, format=None):
        """
        Deletes the object and returns a confirmation message
        """
        return Response({'detail': 'delete request response'}, status=200)

