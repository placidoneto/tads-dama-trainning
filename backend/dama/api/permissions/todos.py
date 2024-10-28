from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

class TodosPodemVer(BasePermission):    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False

class TodosPodemCriar(BasePermission):    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        return False

class TodosPodemEditar(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT' or request.method == 'PATCH':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' or request.method == 'PATCH':
            return True
        return False

class TodosPodemDeletar(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return True
        return False

class TodosTemTodasAsPermissoes(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True
