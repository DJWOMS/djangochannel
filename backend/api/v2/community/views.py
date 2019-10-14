from rest_framework import generics, permissions

from backend.community.models import Groups
from backend.api.v2.community.serializers import GroupsListSerializer


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
    serializer_class = GroupsListSerializer


