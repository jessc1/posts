from rest_framework import routers
from auth.viewsets.register import RegisterViewSet

router = routers.SimpleRouter()
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
    ]
