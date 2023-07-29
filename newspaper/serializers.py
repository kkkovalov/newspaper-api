from newspaper.models import Article, User, Topic, Tag
from rest_framework import serializers

# User related serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password', 'first_name', 'last_name']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        
        if password is not None:
            instance.set_password(password)
            
        instance.save()
        return instance
                

# Articles related serializers

class ArticleSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y%m%d', read_only=True)
    
    class Meta:
        model = Article
        fields = ['name', 'creator', 'created','get_short_body', 'tags', 'topic']
        
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name', 'description']