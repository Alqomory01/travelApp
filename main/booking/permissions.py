from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.role == "admin":
            return True
        
        if user.role == "agent" and obj.agent == user:
            return True

        if user.role == "customer" and obj.customer == user:
            return True

        return False
