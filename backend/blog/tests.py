# from django.test import TestCase
# from django.test import Client
# from django.contrib.auth.models import User
#
# from .models import Post, Tag, BlogCategory, Comment
# from .forms import CommentForm
#
#
# class PostTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         user = User.objects.create(username="Hamel")
#         # tag = Tag.objects.create(name="TagTest")
#         category = BlogCategory.objects.create(name="Категория", active=True, slug="test")
#
#         self.post = Post.objects.create(author_id=user.id,
#                                         title="Test",
#                                         mini_text="Краткое содержание",
#                                         text="Полное содержание",
#                                         created_date="2019-05-05 10:00:00",
#                                         published_date="2019-05-05 10:00:00",
#                                         # tag=tag,
#                                         category=category,
#                                         published=True,
#                                         slug="slug"
#                                         )
#         # Comment.objects.create(user=user,
#         #                        post=post,
#         #                        text="Test comments",
#         #                        date=datetime.datetime.now(),
#         #                        update=datetime.datetime.now(),
#         #                        )
#
#     def test_post(self):
#         text = Post.objects.get(mini_text="Краткое содержание")
#         self.assertEqual(text.mini_text, "Краткое содержание")
#
#     def test_post2(self):
#         post = Post.objects.get(title="Test")
#         self.assertEqual(post.mini_text, 'Краткое содержание')
#
#     def test_list_post(self):
#         response = self.client.get("")
#         self.assertEqual(response.status_code, 200)
#
#     def test_category(self):
#         response = self.client.get("", {"slug": "category"}, {"slug": "test"})
#         self.assertEqual(response.status_code, 200)
#
#     def test_sort_category(self):
#         response = self.client.get("", {"slug": "categories"}, {"slug": "test"})
#         self.assertEqual(response.status_code, 200)
#
#     def test_news(self):
#         response = self.client.get("", {"slug": "test"})
#         self.assertEqual(response.status_code, 200)
#
#     def test_forms(self):
#         form_data = {'text': 'test'}
#         form = CommentForm(data=form_data)
#         self.assertTrue(form.is_valid())
