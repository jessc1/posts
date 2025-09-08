from rest_framework.permissions import IsAuthenticated
from abstract.viewsets import AbstractViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get','patch', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def get_object_by_id(self):
        obj = Post.objects.get(self.kwargs['pk'])
        return obj
        
    def patch(self, request, pk):
        try:
            post = Post.objects.get_object_by_id(pk=pk)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({}, status=status.HTTP_200_OK)