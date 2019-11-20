from rest_framework import serializers

from backend.blog.models import BlogCategory, Tag, Post, Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ListBlogCategoriesSerializer(serializers.ModelSerializer):
    """Сериализация модели категорий и children"""
    children = RecursiveSerializer(many=True)
    link = serializers.URLField(source="get_absolute_url", read_only=True)

    class Meta:
        model = BlogCategory
        fields = ("name", "slug", "link", "children")


class TagSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = Tag
        fields = ("name", "slug")


class ListPostSerializer(serializers.ModelSerializer):
    """Сериализация списка статей"""
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    tag = TagSerializer(many=True)
    comments_count = serializers.IntegerField(source="get_count_comments", read_only=True)
    link = serializers.URLField(source="get_absolute_url", read_only=True)
    published_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "image",
            "mini_text",
            "published_date",
            "category",
            "tag",
            "viewed",
            "comments_count",
            "link"
        )


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    update_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    children = RecursiveSerializer(many=True)
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "user", "text", "created_date", "deleted", "update_date", "children")


class PostDetailSerializer(ListPostSerializer):
    """Сериализация полной статьи"""
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "image",
            "text",
            "published_date",
            "category",
            "tag",
            "description",
            "viewed",
            "comments",
            "comments_count",
        )


class AddPostSerializer(serializers.ModelSerializer):
    """Сериализация добавления статьи"""
    class Meta:
        model = Post
        fields = (
            "title",
            "image",
            "mini_text",
            "text",
            "category",
            "tag",
            "description",
        )


class CreateCommentsSerializer(serializers.ModelSerializer):
    """CRUD comments"""
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")
