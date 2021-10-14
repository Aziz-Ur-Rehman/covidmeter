from rest_framework import permissions


class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Permission for checking if request user and user are same.
    """

    def has_object_permission(self, request, view, obj):
        """
        Implentation for has_permission method that returns true
        if object and request user are same or request method
        is get or options, false otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user == obj:
            return True
        return False
