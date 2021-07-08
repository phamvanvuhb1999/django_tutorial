from rest_framework import permissions
import logging

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owner of an object to edit it
    """
    def has_object_permission(self, request, view, obj):
        #read permission are allowed to any request
        #so we'll always allow GET, HEAD or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True

        #Write permissions are only allowed to the owner of the snippet
        return obj.owner == request.user