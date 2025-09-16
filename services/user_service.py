from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError
from user.models import User
from user.serializers import UserSerializer

class UserService:
    @staticmethod
    def get(user_id):
        try:                       
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise NotFound("User not found")

    @staticmethod
    def list():
        return User.objects.all()