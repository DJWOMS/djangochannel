import datetime
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from backend.blog.models import Post, BlogCategory
from backend.api.v2.blog.serializers import PostSerializer, PostDetailSerializer, BlogCategorySerializer


class PostPagination(PageNumberPagination):
    """Количество записей для пагинации"""
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostList(generics.ListAPIView):
    """Список всех постов"""
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        count = self.request.GET.get("count", None)
        posts = Post.objects.filter(published_date__lte=datetime.datetime.now(), published=True)
        if count is not None:
            posts = posts.order_by()[:int(count)]
        return posts


class PostDetail(generics.RetrieveAPIView):
    """Вывод полной статьи"""
    permission_classes = [permissions.AllowAny]
    serializer_class = PostDetailSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        # TODO переписать данный метод, на получение объекта и его изменение.
        queryset = Post.objects.filter(id=self.kwargs.get('pk'))
        post = Post.objects.get(id=self.kwargs.get('pk'))
        post.viewed += 1
        post.save()
        return queryset


class SortCategory(generics.ListAPIView):
    """Вывод категоий"""
    permission_classes = [permissions.AllowAny]
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    pagination_class = PostPagination

