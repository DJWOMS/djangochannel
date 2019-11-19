from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.dispatch import receiver
from django.db.models.signals import post_save

from backend.comments.models import AbstractComment
from backend.utils.transliteration import transliteration_rus_eng
from backend.utils.send_mail import send_mail_user_post


class BlogCategory(MPTTModel):
    """Класс модели категорий сетей"""
    name = models.CharField("Категория", max_length=50)
    published = models.BooleanField("Опубликовать?", default=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    description = models.TextField("Description", max_length=300, default="")

    def get_absolute_url(self):
        return reverse("list_category", kwargs={"category": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Класс модели тегов"""
    name = models.CharField("Тег", max_length=50, unique=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Post(models.Model):
    """Класс модели поста"""
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE)
    title = models.CharField("Тема", max_length=500)
    mini_text = models.TextField("Краткое содержание", max_length=5000)
    text = models.TextField("Полное содержание", max_length=10000000)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    published_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField("Изображение", upload_to="blog/", blank=True)
    tag = models.ManyToManyField(Tag, verbose_name="Тег", blank=True)
    category = models.ForeignKey(
        BlogCategory,
        verbose_name="Категория",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    published = models.BooleanField("Опубликовать?", default=True)
    viewed = models.IntegerField("Просмотрено", default=0)
    slug = models.SlugField(max_length=500, unique=True)

    description = models.TextField("Description", max_length=300)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_date"]

    def get_category_description(self):
        return self.category.description

    def get_count_comments(self):
        return f"{self.comments.all().count()}"

    def get_comments(self):
        return self.comments.filter(parent=None)

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"category": self.category.slug, "slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = transliteration_rus_eng(self.title) + '-' + datetime.strftime(
                timezone.now(), "%d_%m_%y_%H_%M_%S_%s"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(AbstractComment, MPTTModel):
    """Модель коментариев к новостям"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, verbose_name="Новость", related_name="comments", on_delete=models.CASCADE
    )
    parent = TreeForeignKey(
        "self",
        verbose_name="Родительский комментарий",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{} - {}".format(self.user, self.post)


class SpySearch(models.Model):
    """Модель отслеживания запросов поиска"""
    record = models.CharField("Запрос", max_length=1000)
    counter = models.PositiveIntegerField("Количество запросов", default=0)

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def __str__(self):
        return "{}".format(self.record)


# @receiver(post_save, sender=Post)
# def create_user_post(sender, instance, created, **kwargs):
#     """Отправка сообщения о предложенной статье на email"""
#     if created:
#         send_mail_user_post(instance)
