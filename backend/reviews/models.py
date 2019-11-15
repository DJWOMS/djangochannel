from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    """Модель отзыва"""
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='reviews',
        verbose_name='Пользователь',
        null=True,
        blank=True
    )
    name = models.CharField('Имя', max_length=50)
    text = models.TextField('Текст отзыва', max_length=15000)
    social_link = models.URLField('Ссылка на соц. сеть')
    git_link = models.URLField('Ссылка на git')

    moderated = models.BooleanField('Модерировано', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list_review")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
