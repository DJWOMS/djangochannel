from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from .models import Post, Tag, BlogCategory


class PostTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username="Hamel")
        # tag = Tag.objects.create(name="TagTest")
        category = BlogCategory.objects.create(name="Категория", published=True, slug="test")

        self.post = Post.objects.create(author_id=user.id,
                                        title="Test",
                                        mini_text="Краткое содержание",
                                        text="Полное содержание",
                                        created_date="2019-05-05 10:00:00",
                                        published_date="2019-05-05 10:00:00",
                                        # tag=tag,
                                        category=category,
                                        published=True,
                                        slug="slug"
                                        )

    def test_category(self):
        category = BlogCategory.objects.get(slug="test")
        self.assertEqual(category.name, "Категория")

    def test_post(self):
        post = Post.objects.get(title="Test")
        self.assertEqual(post.mini_text, 'Краткое содержание')
