# Django Rest Framework libraries and packages
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

# Local project packages and functions
from newspaper.views.creator_views import is_creator
from newspaper.models import Tag
from newspaper.serializers import TagSerializer

class TagView(APIView):
    
    
    def get(self, request, format=None):
        """
        Returns all tags from the database. If query parameter 'name' (in slug format) specified in the url, it will return a single object.
        """
        
        # Check whether query has a 'name' field in the url
        if 'name' in request.query_params:
            # retrieve the name and request a QuerySet <> object from the database and serialize it
            slug = request.query_params['name']
            try:
                tag = Tag.objects.get(slug_name=slug)
            except:
                raise exceptions.NotFound
            serializer = TagSerializer(tag)
            
        else:
            # retrieve all object from the database and serialize them
            try:
                tags = Tag.objects.all()
            except:
                raise exceptions.NotFound 
            serializer = TagSerializer(tags, many=True)
            
        # returns object(s) to the client
        return Response(serializer.data, status=200)
    
    
    def post(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Takes a 'name' field and returns a created Tag
        """
        
        # validates that current user is authenticated and has a 'Creator' permission
        if request.user.is_authenticated:
            if is_creator(request.user):
                # serializes new object and after validating data, sends it to the database
                serializer = TagSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                # returns created object to the client
                return Response(serializer.data, status=201)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated
    
    
    def put(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Takes a 'slug_name' to locate the object and 'name' field with updated value. Returns updated object.
        """
        
        # validates that current user is authenticated and has a 'Creator' permission
        if request.user.is_authenticated:
            if is_creator(request.user):
                # checks whether the tag exists in the database, retrieves it and serializes
                try:
                    tag = Tag.objects.get(slug_name=request.data['slug_name'])
                except:
                    raise exceptions.NotFound
                serializer = TagSerializer(tag,request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                # returns updated object to the client
                return Response(serializer.data, status=201)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated
    

    def delete(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Takes a 'slug_name' field and returns OK message upon deletion.
        """
        # validates that current user is authenticated and has a 'Creator' permission
        if request.user.is_authenticated:
            if is_creator(request.user):
                # check whether the tag exists in the database, retrieves it and deletes it
                try:
                    tag = Tag.objects.get(slug_name=request.data['slug_name'])
                except:
                    raise exceptions.NotFound
                tag.delete()
                # returns success message to the client
                return Response({'detail': 'Tag deleted'}, status=200)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated