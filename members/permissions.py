from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to only allow admins to access a view.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

# Permissions to allow regular users

class IsRegularUser(BasePermission):
    """
    Custom permission to only allow regular users (non-admins) to access certain views.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_admin
