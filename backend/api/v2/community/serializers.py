from rest_framework import serializers

from backend.community.models import Groups


class GroupsListSerializer(serializers.ModelSerializer):
    """Сериализация списка групп"""

    class Meta:
        model = Groups
        fields = ("id", "title", "desc", "group_variety", "miniature")


class CreateGroupsSerializer(serializers.ModelSerializer):
    """Сериализация создания группы"""

    class Meta:
        model = Groups
        fields = ("title", "desc", "group_variety", "image")




