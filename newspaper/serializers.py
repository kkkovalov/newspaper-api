from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reader
        fields = ['user.username', 'user.date_joined']
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['name', 'creator', 'created','get_short_body', 'tags', 'topic']
        

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Creator
        fields = ['username','email','department']
