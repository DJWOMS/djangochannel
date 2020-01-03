from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from backend.blog.models import BlogCategory, Post, Tag, Comment
from .serializers import ListPostSerializer


class BlogTest(APITestCase):
    """Тесты блога"""
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Hamel")

        category = BlogCategory.objects.create(name="Test category",
                                               published=True,
                                               slug="test_category")

        tag = Tag.objects.create(name="Test teg", slug="test_slug")

        post = Post.objects.create(author=user,
                                   title="Test post",
                                   mini_text="Mini_text",
                                   text="Text",
                                   created_date="2019-05-25",
                                   published_date="2019-05-28",
                                   category=category,
                                   published=True,
                                   viewed=0,
                                   slug="test_post")
        post.tag.add(tag)

    def test_post(self):
        """Есть ли post в бд"""
        post = Post.objects.get(title="Test post")
        self.assertEqual(post.mini_text, "Mini_text")

    def test_post_list(self):
        """Тест списка статей"""
        response = self.client.get(reverse("list_post"))
        serializer = ListPostSerializer(Post.objects.filter(published=True), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.json().get("results"))
#
#     # def test_post_detail(self):
#     #     user = User.objects.get(username="Hamel")
#     #     request = self.factory.get(self.post_detail_url, pk=1)
#     #     force_authenticate(request, user=user)
#     #     response = self.post_detail_view(request)
#     #     response.render()
#     #     res = json.loads(response.content)
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_category(self):
#         user = User.objects.get(username="Hamel")
#         request = self.factory.get(self.sort_category_url)
#         force_authenticate(request, user=user)
#         response = self.sort_category_view(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_sort_post_category(self):
#         user = User.objects.get(username="Hamel")
#         request = self.factory.get(self.sort_post_category_url, {'slug': 'test_category'})
#         force_authenticate(request, user=user)
#         response = self.sort_post_category_view(request)
#         response.render()
#         res = json.loads(response.content)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
#
