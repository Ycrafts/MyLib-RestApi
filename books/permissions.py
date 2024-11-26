from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsAdminUserForCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    

# class ReadOnlyOrAuthenticatedWrite(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True  # SAFE methods (GET, HEAD, OPTIONS) are allowed for everyone
#         return request.user and request.user.is_authenticated