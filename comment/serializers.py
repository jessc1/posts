from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from abstract.serializers import AbstractSerializer
from user.models import User
from user.serializers import UserSerializer
from comment.models import Comment 
from post.models import Post

class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')

    class Meta:
            model = Comment
            fields = ['id', 'author', 'post', 'body']
    
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
    
   

    
    
