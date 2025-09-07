from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from abstract.serializers import AbstractSerializer
from user.models import User
from .models import Post

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
            model = Post
            fields = ['id', 'author', 'created', 'updated', 'title', 'content']

    

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("Not permitted create post for the following user")
        return value

        
        