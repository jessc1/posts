from rest_framework import routers
from .viewsets import CommentViewSet
from post.viewsets import PostViewSet
from rest_framework_nested.routers import NestedSimpleRouter


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
post_comments =NestedSimpleRouter(router, 'posts', lookup='posts')
post_comments.register(r'comment', CommentViewSet, basename='post-comment')
router.register(r'comment', CommentViewSet , basename='comment')
urlpatterns = [
    *router.urls,
    *post_comments.urls,
]
