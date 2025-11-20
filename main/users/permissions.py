# users/permissions.py
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to users with role 'admin'
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsAgent(BasePermission):
    """
    Allows access only to users with role 'agent'
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'agent'


class IsCustomer(BasePermission):
    """
    Allows access only to users with role 'customer'
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'
