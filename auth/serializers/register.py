from rest_framework import serializers
from user.serializers import UserSerializer
from user.models import User

class RegisterSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
