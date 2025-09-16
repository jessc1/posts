from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError
from post.models import Post
from post.serializers import PostSerializer

class PostService:
    @staticmethod
    def list():
        return Post.objects.all()

    @staticmethod
    def get(user_id):
        try:                       
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise NotFound("User not found")
    
    @staticmethod
    @transaction.atomic
    def create(post):
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        raise ValidationError("Invalid post data")
    
    @staticmethod
    @transaction.atomic
    def patch(id, data):
        try: 
            post = Post.objetcs.get(id=id)
        except ObjectDoesNotExist:
            raise NotFound("Post not found")
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        raise ValidationError("Invalid Post")
    
    @staticmethod
    @transaction.atomic
    def delete(id):
        try:
            post = Post.objects.get(id=id)
            post.delete()
        except ObjectDoesNotExist:
            raise NotFound("Post not found")

    



  