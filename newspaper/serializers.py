from newspaper.models import Article, User
from rest_framework import serializers

# User related serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
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
        

# Articles related serializers

class ArticleSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y%m%d', read_only=True)
    
    class Meta:
        model = Article
        fields = ['name', 'creator', 'created','get_short_body', 'tags', 'topic']
     