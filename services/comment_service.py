from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError
from comment.models import Comment
from comment.serializers import CommentSerializer

class CommentService:
    @staticmethod
    def list():
        return Comment.objects.all()

    @staticmethod
    def get(id):
        try:                       
            return Comment.objects.get(id=id)
        except ObjectDoesNotExist:
            raise NotFound("Comment not found")
    
    @staticmethod
    @transaction.atomic
    def create(comment):
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        raise ValidationError("Invalid comment")
    
    @staticmethod
    @transaction.atomic
    def patch(id, data):
        try: 
            comment = Comment.objetcs.get(id=id)
        except ObjectDoesNotExist:
            raise NotFound("Comment not found")
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        raise ValidationError("Invalid Comment")
    
    @staticmethod
    @transaction.atomic
    def delete(id):
        try:
            comment = Comment.objects.get(id=id)
            comment.delete()
        except ObjectDoesNotExist:
            raise NotFound("Comment not found")

    



  