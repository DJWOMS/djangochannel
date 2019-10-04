# from django.test import Client
# from django.contrib.auth.models import User
# from kombu.utils import json
# from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
# from rest_framework import status
#
# from backend.blog.models import BlogCategory, Post, Tag
# from .views import PostList, PostDetail, SortCategory, SortPostCategory
#
#
# class SimpleTest(APITestCase):
#     def setUp(self):
#         self.client = Client()
#         self.factory = APIRequestFactory()
#
#         self.post_list_url = ""
#         self.post_detail_url = '/detail/'
#         self.sort_category_url = '/sort_category/'
#         self.sort_post_category_url = '/sort_post/'
#
#         self.post_list_view = PostList.as_view()
#         self.post_detail_view = PostDetail.as_view()
#         self.sort_category_view = SortCategory.as_view()
#         self.sort_post_category_view = SortPostCategory.as_view()
#
#     @classmethod
#     def setUpTestData(cls):
#         user = User.objects.create(username="Hamel")
#
#         category = BlogCategory.objects.create(name="Test category",
#                                                active=True,
#                                                slug="test_category")
#
#         tag = Tag.objects.create(name="Test teg", slug="test_slug")
#
#         post = Post.objects.create(author=user,
#                                    title="Test post",
#                                    mini_text="Mini_text",
#                                    text="Text",
#                                    created_date="2019-05-25 10:00:00.000000",
#                                    published_date="2019-05-28 10:00:00.000000",
#                                    category=category,
#                                    published=True,
#                                    viewed=0,
#                                    slug="test_post")
#         tg = post.tag.add(tag)
#         print(post.id)
#
#     def test(self):
#         post = Post.objects.get(title="Test post")
#         self.assertEqual(post.mini_text, "Mini_text")
#
#     def test_post_list(self):
#         user = User.objects.get(username="Hamel")
#         request = self.factory.get(self.post_list_url)
#         force_authenticate(request, user=user)
#         response = self.post_list_view(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
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
