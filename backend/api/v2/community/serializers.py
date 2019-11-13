from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from backend.community.models import Groups, EntryGroup, CommentEntryGroup


class CreateCommentEntryGroupSerializer(serializers.ModelSerializer):
    """Добавление комментариев записей в группе"""
    class Meta:
        model = CommentEntryGroup
        fields = ("entry", "text")


class ListCommentEntryGroupSerializer(serializers.ModelSerializer):
    """Список комментариев записей в группе"""
    children = serializers.ListField(source='get_children', read_only=True, child=RecursiveField())

    class Meta:
        model = CommentEntryGroup
        fields = ("id", "entry", "text", "children")


class GroupsListSerializer(serializers.ModelSerializer):
    """Сериализация списка групп"""

    class Meta:
        model = Groups
        fields = ("id", "title", "desc", "group_variety", "miniature")


class CreateGroupsSerializer(serializers.ModelSerializer):
    """Сериализация создания группы"""

    class Meta:
        model = Groups
        fields = ("title", "desc", "group_variety", "image", "miniature")


class EntryGroupSerializer(serializers.ModelSerializer):
    """Вывод и редактирование записи в группе"""
    author = serializers.ReadOnlyField(source='author.username')
    comment = ListCommentEntryGroupSerializer(many=True, read_only=True)

    class Meta:
        model = EntryGroup
        fields = ("id", "created_date", "author", "group", "title", "text", "comment")


class EntriesGroupSerializer(serializers.ModelSerializer):
    """Список записей в группе"""
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = EntryGroup
        fields = ("id", "created_date", "author", "group", "title", "text", "comments_count")


class GroupSerializer(serializers.ModelSerializer):
    """Группа и список записей в группе"""
    entry = EntriesGroupSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ("id", "title", "desc", "group_variety", "image", "miniature", "entry")
