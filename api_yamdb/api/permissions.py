from rest_framework import permissions

class CustomIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        #if request.user.role == 'admin'
        return request.user.role == 'admin'
        