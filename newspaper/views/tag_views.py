from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from newspaper.views.creator_views import is_creator
from newspaper.models import Tag
from newspaper.serializers import TagSerializer

class TagView(APIView):
    
    def get(self, request, format=None):
        """
        Returns all tags from the database. If query parameter 'slug_name' specified in the url, it will return a single object.
        """
        if 'slug_name' in request.query_params:
            slug = request.query_params['slug_name']
            try:
                tag = Tag.objects.get(slug_name=slug)
            except:
                raise exceptions.NotFound
            serializer = TagSerializer(tag)
            return Response(serializer.data, status=200)
        else:
            try:
                tags = Tag.objects.all()
            except:
                raise exceptions.NotFound
            serializer = TagSerializer(tags, many=True)
            return Response(serializer.data, status=200)
    
    def post(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Takes a 'name' field and returns a created Tag
        """
        if request.user.is_authenticated:
            if is_creator(request.user):
                serializer = TagSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated
    
    def put(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Takes a 'slug_name' to locate the object and 'name' field with updated value. Returns updated object.
        """
        if request.user.is_authenticated:
            if is_creator(request.user):
                try:
                    tag = Tag.objects.get(slug_name=request.data['slug_name'])
                except:
                    raise exceptions.NotFound
                serializer = TagSerializer(tag,request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated
    
    def delete(self, request, format=None):
        """
        Creator permission and authentication required to access this request. Takes a 'slug_name' field and returns OK message upon deletion.
        """
        if request.user.is_authenticated:
            if is_creator(request.user):
                try:
                    tag = Tag.objects.get(slug_name=request.data['slug_name'])
                except:
                    raise exceptions.NotFound
                tag.delete()
                return Response({'detail': 'Tag deleted'}, status=200)
            else:
                raise exceptions.PermissionDenied
        else:
            raise exceptions.NotAuthenticated