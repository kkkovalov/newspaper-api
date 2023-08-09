from newspaper.models import Article, Topic, Tag
from rest_framework import serializers

# Articles related serializers

class ArticleSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y%m%d', read_only=True)
    
    class Meta:
        model = Article
        fields = ['name', 'creator', 'created','get_short_body', 'tags', 'topic']
        
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name', 'description', 'slug_name']
        read_only_fields = ['slug_name']
        
# Tag serializer for Tag model. Serializes 'name' and 'slug_name' fields, returns both fields with default ordering by 'name'
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug_name']
        read_only_fields = ['slug_name']