import datetime

from django_filters import rest_framework as filters, ModelChoiceFilter
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


# class ProductFilter(filters.FilterSet):
#     category = ModelChoiceFilter(queryset=BlogCategory.objects.all())
#
#     class Meta:
#         model = Post
#         fields = ["category__slug"]
#             #'tag': ['tag__slug'],
#             # 'category': ['slug'],"published_date__lte",


class PostListView(generics.ListAPIView):
    """Список всех постов"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.filter(published_date__lte=datetime.datetime.now(), published=True)
    serializer_class = ListPostSerializer
    pagination_class = PostPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get("category"):
            queryset = queryset.filter(category__slug=self.kwargs.get("category"))
        # elif self.kwargs.get('tag') is not None:
        #     queryset = self.queryset.filter(tag__slug=self.kwargs.get('tag'))
        return queryset


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
