from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from backend.blog.models import BlogCategory, Tag, Post


class BlogCategorySerializer(serializers.ModelSerializer):
    """Сериализация модели категорий"""
    children = serializers.ListField(source='get_children', read_only=True,
                                     child=RecursiveField(), )

    class Meta:
        model = BlogCategory
        fields = ("id", "name", "children", "slug")


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


class PostSerializer(serializers.ModelSerializer):
    """Сериализация списка статей"""
    category = BlogCategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id",
                  "title",
                  "mini_text",
                  "created_date",
                  "category",
                  "tag",
                  "viewed")


class SortPostSerializer(serializers.ModelSerializer):
    """Сериализация постов по категории"""
    category = SortPostCategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id",
                  "title",
                  "mini_text",
                  "created_date",
                  "category",
                  "tag",
                  "viewed")


class PostDetailSerializer(serializers.ModelSerializer):
    """Сериализация полной статьи"""
    category = BlogCategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id",
                  "author",
                  "title",
                  "text",
                  "image",
                  "created_date",
                  "category",
                  "tag",
                  "viewed")

