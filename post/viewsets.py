from abstract.viewsets import AbstractViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from auth.permissions import UserPermission
from rest_framework.decorators import action
from django.core.cache import cache
from services.post_service import PostService
import logging

logger = logging.getLogger( __name__ )

class PostViewSet(AbstractViewSet):
    http_method_names = ('post','get','patch', 'delete')
    permission_classes = (UserPermission,)
    ordering_fields = ['author', 'title', 'content']
    ordering = ['title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'author__username']
    serializer_class = PostSerializer

    def get_queryset(self):
        logger.info("Post requests")
        posts = cache.get('post_objects')
        if not posts:
            posts = PostService.list()          
            cache.set('post_objects', posts)
        return posts
        
    
    def get_object_by_id(self):
        post = PostService.get(self.kwargs['pk'])
        return post
        
    def patch(self, request, pk):
        post = PostService.patch(request.data, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        PostService.delete(pk)
        return Response({}, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user

        user.like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=True)
    def remove_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.remove_like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
