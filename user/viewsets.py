from rest_framework import viewsets
from abstract.viewsets import AbstractViewSet
from user.serializers import UserSerializer
from user.models import User
from django.core.cache import cache
from auth.permissions import UserPermission


class UserViewSet(AbstractViewSet):
    http_method_names = ('patch',  'get')
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()  
        return User.objects.exclude(is_superuser=True)
    
    def get_object_by_id(self):
        obj = User.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj