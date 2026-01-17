from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admins to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsStudentUser(permissions.BasePermission):
    """
    Custom permission to only allow students to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_student

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user