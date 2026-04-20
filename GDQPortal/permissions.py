from rest_framework import permissions

class IsEditorOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow editors and admins to edit.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role in ['editor', 'admin']

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'