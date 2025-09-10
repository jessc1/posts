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
    liked = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
            model = Comment
            fields = ['id', 'author', 'post', 'body', 'liked', 'likes']
    
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
    
    def get_liked(self, instance):
        request = self.context.get("request", None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked_comment(instance)
    
    def get_likes(self, instance):
        return instance.commented_by.count()
    
   

    
    
