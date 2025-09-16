from rest_framework import viewsets
from abstract.viewsets import AbstractViewSet
from user.serializers import UserSerializer
from user.models import User
from auth.permissions import UserPermission
from services.user_service import UserService


class UserViewSet(AbstractViewSet):
    http_method_names = ('patch',  'get')
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer

    def get_queryset(self):
        users = UserService.list()
        if self.request.user.is_superuser:
            return users
        return users.objects.exclude(is_superuser=True)
    
    def get_object_by_id(self):
        user = UserService.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, user)
        return user