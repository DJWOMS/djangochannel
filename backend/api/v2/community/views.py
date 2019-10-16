from rest_framework import generics, permissions
from rest_framework.response import Response

from backend.community.models import Groups, EntryGroup
from backend.api.v2.community.serializers import (
    GroupsListSerializer, CreateGroupsSerializer, EntryGroupSerializer)


class GroupListView(generics.ListAPIView):
    """Вывод списка групп"""
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupsListSerializer

    def get_queryset(self):
        return Groups.objects.exclude(group_variety="private")


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
    # serializer_class =

    def post(self, request, **kwargs):
        group = self.get_object()
        group.members.add(request.user)
        return Response(status=201)


class CreateEntryGroup(generics.CreateAPIView):
    """Создание записи в группе"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = EntryGroup.objects.all()
    serializer_class = EntryGroupSerializer

    def create(self, request, *args, **kwargs):
        if Groups.objects.filter(id=int(request.data.get("group")), members=request.user).exists():
            super().create(request, *args, **kwargs)
        else:
            return Response(status=404)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, gruop=int(self.request.data.get("group")))