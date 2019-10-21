from rest_framework import generics, permissions, mixins, decorators
from rest_framework.response import Response

from backend.api.v2.community.permissions import IsMemberGroup, IsAuthorEntry
from backend.community.models import Groups, EntryGroup
from backend.api.v2.community.serializers import (
    GroupsListSerializer, CreateGroupsSerializer, EntryGroupSerializer, GroupSerializer)


class GroupListView(generics.ListAPIView):
    """Вывод списка групп"""
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupsListSerializer

    def get_queryset(self):
        return Groups.objects.exclude(group_variety="private")


class GroupView(generics.RetrieveAPIView):
    """Вывод группы"""
    permission_classes = [permissions.AllowAny]
    queryset = Groups.objects.filter(group_variety="open")
    serializer_class = GroupSerializer


class CreateGroupView(generics.CreateAPIView):
    """Создание группы"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Groups.objects.all()
    serializer_class = CreateGroupsSerializer

    def perform_create(self, serializer):
        serializer.save(founder=self.request.user)


class GroupAddMember(generics.GenericAPIView):
    """Вступление в группу"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Groups.objects.filter(group_variety="open")

    def post(self, request, **kwargs):
        group = self.get_object()
        group.members.add(request.user)
        return Response(status=201)

    def delete(self, request, **kwargs):
        group = self.get_object()
        group.members.remove(request.user)
        return Response(status=204)


class EntryGroupView(generics.CreateAPIView,
                     generics.RetrieveAPIView,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    """Редактирование записи в группе"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMemberGroup]
    queryset = EntryGroup.objects.all()
    serializer_class = EntryGroupSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # @decorators.permission_classes(IsAuthorEntry)
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user or instance.group.founder == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=404)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user or instance.group.founder == request.user:
            return super().destroy(request, *args, **kwargs)


class CommentsEntryGroupView(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    """Редактирование записи в группе"""
    pass













