from rest_framework import serializers
from abstract.serializers import AbstractSerializer
from user.models import User
from django.conf import settings

class UserSerializer(AbstractSerializer):
    id = serializers.IntegerField(label="User ID", read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        avatar_url = representation.get("avatar")
        if not avatar_url:
            representation["avatar"] = settings.DEFAULT_AVATAR_URL
        return representation

    class Meta:
        model = User 
        fields = [
            'id', 'username', 'email', 'avatar','created', 'updated'
        ]
