from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):        
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if request.user.is_authenticated:
            return True
      
        return False
    
    def has_permission(self, request, view):       
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        if request.user.is_authenticated:
            return True
        return False