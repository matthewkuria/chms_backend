from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin

class IsSecretary(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_secretary

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_member
