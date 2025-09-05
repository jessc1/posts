from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from user.serializers import UserSerializer
from user.models import User

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch',  'get')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object_by_id(self):
        obj = User.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj