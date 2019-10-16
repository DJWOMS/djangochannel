from rest_framework import serializers

from backend.community.models import Groups, EntryGroup


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


class EntryGroupSerializer(serializers.ModelSerializer):
    """Редактирование записи в группе"""
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = EntryGroup
        fields = ("id", "created_date", "author", "group", "title", "text")


class GroupSerializer(serializers.ModelSerializer):
    """Группа и список записей в группе"""
    entry = EntryGroupSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ("id", "title", "desc", "group_variety", "image", "miniature", "entry")