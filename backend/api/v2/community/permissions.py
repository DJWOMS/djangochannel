from rest_framework.permissions import BasePermission


class IsMemberGroup(BasePermission):
    """Участик группы или админимтратор"""
    def has_object_permission(self, request, view, obj):
        return request.user in obj.group.members.all() or obj.group.founder == request.user


class IsAuthorEntry(BasePermission):
    """Автор записи или админимтратор"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.group.founder == request.user


class IsAuthorCommentEntry(BasePermission):
    """Автор комментария или админимтратор"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.entry.group.founder == request.user