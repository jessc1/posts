from rest_framework.permissions import IsAuthenticated
from abstract.viewsets import AbstractViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get')
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def get_object_by_id(self):
        obj = Post.objects.get(self.kwargs['pk'])
        return obj
