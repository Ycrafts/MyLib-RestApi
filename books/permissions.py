from rest_framework import permissions

class IsAdminUserForCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user and request.user.is_staff
    
#no has_object_permission class needed since we got no need for accessing the creator of the obj 