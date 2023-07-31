from django.utils.text import slugify

# rest_framework packages
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions

# local packages
from newspaper.models import Topic
from newspaper.serializers import TopicSerializer
from newspaper.views.creator_views import is_creator
    
class TopicView(APIView):
    
    def get(self, request, format=None):
        """
        Returns a list of JSON objects, if they exist in the database. No request body required.
        """
        
        # checks whether 'name' query parameter is specified in the url and retrieves it contents
        if 'name' in request.query_params:
            slug = request.query_params['name']
            # gets the object by slug_name and serializes it
            try:
                topic = Topic.objects.get(slug_name=slug)
            except:
                raise exceptions.NotFound
            serializer = TopicSerializer(topic)
        else:
            # gets all the topics from the database and serializes them
            try:
                topics_list = Topic.objects.all()
            except:
                raise exceptions.NotFound
            serializer = TopicSerializer(topics_list, many=True)
            
        # returns serialized data to the client
        return Response(serializer.data, status=200)
    
    
    def post(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Returns created topic to the client upon successful request.
        """
        
        # Verifies that user has required permissions and authenticated to access the request
        if request.user.is_authenticated:
            if is_creator(request.user):
                # serializes parsed data and validates it before saving
                try:
                    topic = TopicSerializer(data=request.data)
                except:
                    raise exceptions.ErrorDetail
                topic.is_valid(raise_exception=True)
                topic.save()
                # returns created object to the client
                return Response(topic.data, status=201)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.AuthenticationFailed
    
    
    def put(self, request, format=None):
        """
        Takes JSON object with keys (name, description). Returns updated object.
        """
        
        # Verifies that user has required permissions and authenticated to access the request
        if request.user.is_authenticated:
            if is_creator(request.user):
                # retrieves an object from the database by 'slug_name'
                try:
                    topic = Topic.objects.get(slug_name=request.data['slug_name'])
                except:
                    raise exceptions.NotFound
                # serializes and validates the object before saving it to the database
                serializer = TopicSerializer(topic, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                # returns updated object back to the user
                return Response(serializer.data, status=200)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.AuthenticationFailed
    
    
    def delete(self, request, format=None):
        """
        Deletes the object and returns a confirmation message
        """
        # Verifies that user has required permissions and authenticated to access the request
        if request.user.is_authenticated:
            if is_creator(request.user):
                # retrieves the topic from the database by the 'slug_name'
                try:
                    topic = Topic.objects.get(slug_name=request.data['slug_name'])
                except:
                    raise exceptions.NotFound
                # delets an object and returns a confirmation message
                topic.delete()
                return Response({'detail': 'Topic deleted'}, status=200)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.AuthenticationFailed

