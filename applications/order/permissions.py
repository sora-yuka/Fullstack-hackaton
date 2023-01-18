from rest_framework.permissions import BasePermission

class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (obj.owner == request.user or request.user.is_staff)