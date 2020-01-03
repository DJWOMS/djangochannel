from rest_framework import serializers

from backend.api.v2.viewsets.serializers import FilterCommentListSerializer, RecursiveSerializer
from backend.blog.models import BlogCategory, Tag, Post, Comment


class ListBlogCategoriesSerializer(serializers.ModelSerializer):
    """Сериализация модели категорий и children"""
    children = RecursiveSerializer(many=True)
    link = serializers.URLField(source="get_absolute_url", read_only=True)

    class Meta:
        model = BlogCategory
        fields = ("name", "slug", "link", "children")


class BlogCategoriesSerializer(serializers.ModelSerializer):
    """Сериализация модели категорий"""
    class Meta:
        model = BlogCategory
        fields = ("name", "description")


class TagSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = Tag
        fields = ("name", "slug")


class ListPostSerializer(serializers.ModelSerializer):
    """Сериализация списка статей"""
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    # link = serializers.URLField(source="get_absolute_url", read_only=True)
    category = BlogCategoriesSerializer(read_only=True)
    tag = TagSerializer(many=True)
    comments_count = serializers.IntegerField(source="get_count_comments", read_only=True)

    class Meta:
        model = Post
        exclude = ("text", "created_date", "published") #, "slug")


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "user", "text", "created_date", "update_date", "deleted", "children")


class PostDetailSerializer(ListPostSerializer):
    """Сериализация полной статьи"""
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ("mini_text", "created_date", "published", "slug")


class AddPostSerializer(serializers.ModelSerializer):
    """Сериализация добавления статьи"""
    class Meta:
        model = Post
        fields = ("title", "image", "mini_text", "text", "category", "tag", "description")


class CreateCommentsSerializer(serializers.ModelSerializer):
    """CRUD comments"""
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")
