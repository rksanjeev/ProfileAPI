from rest_framework import permissions

class UpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS :
            return True
        else:
            return object.id == request.user.id


class UpdateStatus(permissions.BasePermission):
    """Restrict user to update self created status messages"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user.id == request.user.id
