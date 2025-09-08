from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from abstract.serializers import AbstractSerializer
from user.models import User
from user.serializers import UserSerializer
from .models import Post

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    liked = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
            model = Post
            fields = ['id', 'author', 'created', 'updated', 'title', 'content', 'liked', 'likes']    

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("Not permitted create post for the following user")
        return value
    
    def get_liked(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)
    
    def get_likes(self, instance):
        return instance.liked_by.count()

    
    

   

        
        