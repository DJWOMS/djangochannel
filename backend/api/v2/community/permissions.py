from django.db.models import Q
from rest_framework.permissions import BasePermission


class IsMemberGroup(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.group.members.all() or obj.group.founder == request.user


class IsAuthorEntry(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.group.founder == request.user