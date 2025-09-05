from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label="User ID", read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User 
        fields = [
            'id', 'username', 'email', 'created', 'updated'
        ]
