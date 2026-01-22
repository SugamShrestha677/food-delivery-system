<<<<<<< HEAD
# permissions.py
from rest_framework.permissions import BasePermission

class IsDeliveryPerson(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'driver'
=======
# permissions.py
from rest_framework.permissions import BasePermission

class IsDeliveryPerson(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'driver'
>>>>>>> 39a144b3f68ac0f01775da573343fc5bd5d79b38
