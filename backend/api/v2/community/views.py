from rest_framework import generics, permissions
from rest_framework.response import Response

from backend.api.v2.viewsets.classes import CreateUpdateDestroyDS, CreateRetrieveUpdateDestroyDS
from backend.api.v2.viewsets.permissions import IsMemberGroup, IsAuthorEntry, IsAuthorCommentEntry
from backend.community.models import Groups, EntryGroup, CommentEntryGroup
from backend.api.v2.community.serializers import (
    GroupsListSerializer, CreateGroupsSerializer, EntryGroupSerializer, GroupSerializer,
    CreateCommentEntryGroupSerializer)


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


class EntryGroupView(CreateRetrieveUpdateDestroyDS):
    """Редактирование записи в группе"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMemberGroup]
    queryset = EntryGroup.objects.all()
    serializer_class = EntryGroupSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthorEntry],
                                    'destroy': [IsAuthorEntry]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsEntryGroupView(CreateUpdateDestroyDS):
    """Редактирование комментариев к запси"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMemberGroup]
    queryset = CommentEntryGroup.objects.all()
    serializer_class = CreateCommentEntryGroupSerializer
    permission_classes_by_action = {'update': [IsAuthorCommentEntry],
                                    'destroy': [IsAuthorCommentEntry]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
