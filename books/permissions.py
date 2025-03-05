from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsAdminUserForCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    
class IsAuthenticatedUserForCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        if request.method in permissions.SAFE_METHODS or request.method == "POST" or request.method == "DELETE":
            return True
        
        return request.user and request.user.is_staff
        
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return request.user and request.user.is_staff
    
    
# class ReadOnlyOrAuthenticatedWrite(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True  # SAFE methods (GET, HEAD, OPTIONS) are allowed for everyone
#         return request.user and request.user.is_authenticated