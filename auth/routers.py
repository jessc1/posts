from rest_framework import routers
from auth.viewsets.register import RegisterViewSet
from auth.viewsets.login import LoginViewSet
from auth.viewsets.refresh import RefreshViewSet
from auth.viewsets.logout import LogoutViewSet

router = routers.SimpleRouter()
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'auth/logout', LogoutViewSet, basename='auth-logout')




urlpatterns = [
    *router.urls,
    ]
