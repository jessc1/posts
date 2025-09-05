from rest_framework import routers
from auth.viewsets.register import RegisterViewSet
from auth.viewsets.login import LoginViewSet

router = routers.SimpleRouter()
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')

urlpatterns = [
    *router.urls,
    ]
