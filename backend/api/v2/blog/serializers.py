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
        fields = ("name", "slug")


class SortPostCategorySerializer(serializers.ModelSerializer):
    """Сериализация категории сортировки постов"""

    class Meta:
        model = BlogCategory
        fields = ("id", "name", "slug")


class TagSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = Tag
        fields = ("id", "name")


class ListPostSerializer(serializers.ModelSerializer):
    """Сериализация списка статей"""
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    category = BlogCategorySerializer(read_only=True)
    tag = TagSerializer(many=True)
    comments_count = serializers.IntegerField(source="get_count_comments", read_only=True)
    link = serializers.URLField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "mini_text",
            "created_date",
            "category",
            "tag",
            "viewed",
            "comments_count",
            "link"
        )


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ("user", "text", "created_date", "update_date")


class PostDetailSerializer(serializers.ModelSerializer):
    """Сериализация полной статьи"""
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    category = BlogCategorySerializer()
    tag = TagSerializer(many=True)
    comments = CommentsSerializer(read_only=True)
    comments_count = serializers.IntegerField(source="get_count_comments", read_only=True)
    created_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "text",
            "image",
            "created_date",
            "category",
            "tag",
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
