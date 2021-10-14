from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission for checking if the object belongs to the user himself.
    """

    def has_object_permission(self, request, view, obj):
        """
        Implentation for has_permission method that returns true
        if object's owner and request user are same, false otherwise.
        """
        return obj.user == request.user
