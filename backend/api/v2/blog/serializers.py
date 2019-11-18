from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from backend.blog.models import BlogCategory, Tag, Post, Comment


class ListBlogCategoriesSerializer(serializers.ModelSerializer):
    """Сериализация модели категорий и детей"""
    children = serializers.ListField(
        source='get_children', read_only=True, child=RecursiveField()
    )

    class Meta:
        model = BlogCategory
        fields = ("id", "name", "children", "slug")


class BlogCategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий"""

    class Meta:
        model = BlogCategory
        fields = ("name",)


class SortPostCategorySerializer(serializers.ModelSerializer):
    """Сериализация категории сортировки постов"""

    class Meta:
        model = BlogCategory
        fields = ("name", "slug", "description")


class TagSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = Tag
        fields = ("id", "name")


class ListPostSerializer(serializers.ModelSerializer):
    """Сериализация списка статей"""
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    tag = TagSerializer(many=True)
    comments_count = serializers.IntegerField(source="get_count_comments", read_only=True)
    link = serializers.URLField(source="get_absolute_url", read_only=True)
    created_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "image",
            "mini_text",
            "created_date",
            "category",
            "tag",
            "viewed",
            "comments_count",
            "link"
        )


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только perents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveCommentSerializer(serializers.Serializer):
    """Вывод children в коментариях"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    update_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    children = RecursiveCommentSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("user", "text", "created_date", "update_date", "children")


class PostDetailSerializer(ListPostSerializer):
    """Сериализация полной статьи"""
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "image",
            "text",
            "created_date",
            "category",
            "tag",
            "description",
            "viewed",
            "comments",
            "comments_count",
        )


class SortPostSerializer(serializers.ModelSerializer):
    """Сериализация постов по категории"""
    category = SortPostCategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "mini_text",
            "created_date",
            "category",
            "tag",
            "viewed"
        )
