import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from backend.blog.models import Post, BlogCategory
from backend.api.v2.blog.serializers import (
    ListPostSerializer, PostDetailSerializer, BlogCategorySerializer
)


class PostPagination(PageNumberPagination):
    """Количество записей для пагинации"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListView(generics.ListAPIView):
    """Список всех постов"""
    permission_classes = [permissions.AllowAny]
    serializer_class = ListPostSerializer
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category', 'tag']

    def get_queryset(self):
        count = self.request.GET.get("count", None)
        posts = Post.objects.filter(published_date__lte=datetime.datetime.now(), published=True)
        if count is not None:
            posts = posts.order_by()[:int(count)]
        return posts


class PostDetailView(generics.RetrieveAPIView):
    """Вывод полной статьи"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.filter(published_date__lte=datetime.datetime.now(), published=True)
    serializer_class = PostDetailSerializer
    lookup_field = "slug"

    def get_object(self):
        obj = super().get_object()
        obj.viewed += 1
        obj.save()
        return obj


class CategoriesView(generics.ListAPIView):
    """Вывод категоий"""
    permission_classes = [permissions.AllowAny]
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

