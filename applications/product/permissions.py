from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsProductOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated or request.user.is_staff
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user == obj.owner
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)
    
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if  request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated or request.user.is_staff
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user == obj.owner
        else:
            return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)
    
    