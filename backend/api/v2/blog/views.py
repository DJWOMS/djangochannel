# from datetime import datetime
from django.utils import timezone
from django_filters import rest_framework as rest_filters, NumberFilter, CharFilter
from rest_framework import filters
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from backend.api.v2.viewsets.permissions import IsAuthorComment
from backend.blog.models import Post, BlogCategory, Comment
from backend.api.v2.blog.serializers import (
    ListPostSerializer, PostDetailSerializer, ListBlogCategoriesSerializer, AddPostSerializer,
    CreateCommentsSerializer
)


class PostPagination(PageNumberPagination):
    """Количество записей для пагинации"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostFilter(rest_filters.FilterSet):
    """Фильтр статей"""
    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    tag = CharFilter(field_name='tag__name', lookup_expr='icontains')
    year = NumberFilter(field_name='published_date', lookup_expr='year')
    month = NumberFilter(field_name='published_date', lookup_expr='month')

    class Meta:
        model = Post
        fields = ['tag', 'category', 'published_date']


class PostListView(generics.ListAPIView):
    """Список всех постов"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.filter(published_date__lte=timezone.now(), published=True)
    serializer_class = ListPostSerializer
    pagination_class = PostPagination
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = PostFilter
    search_fields = ['title', 'category__name', 'tag__name']


class PostDetailView(generics.RetrieveAPIView):
    """Вывод полной статьи"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.filter(published_date__lte=timezone.now(), published=True)
    serializer_class = PostDetailSerializer
    lookup_field = "pk"

    def get_object(self):
        obj = super().get_object()
        obj.viewed += 1
        obj.save()
        return obj


class CreatePostView(generics.CreateAPIView):
    """Добавление статьи пользователем"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, published=False)


class CategoriesView(generics.ListAPIView):
    """Вывод категоий"""
    permission_classes = [permissions.AllowAny]
    queryset = BlogCategory.objects.filter(parent=None)
    serializer_class = ListBlogCategoriesSerializer


class CommentsView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    """CRUD comment"""
    permission_classes = [IsAuthorComment]
    queryset = Comment.objects.filter(deleted=False)
    serializer_class = CreateCommentsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
