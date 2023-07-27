from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers

# User related serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Articles related serializers

class ArticleSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y%m%d', read_only=True)
    
    class Meta:
        model = models.Article
        fields = ['name', 'creator', 'created','get_short_body', 'tags', 'topic']
     