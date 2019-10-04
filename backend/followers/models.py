from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Followers(models.Model):
    """Модель друзей и подписчиков"""
    subscribed = models.ForeignKey(
        User,
        related_name="owner",
        verbose_name="На кого подписаны",
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    friends = models.ForeignKey(
        User,
        verbose_name="Кто подписан",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    in_friends = models.BooleanField("В друзьях", default=False)
    in_followers = models.BooleanField("В подписчиках", default=False)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    def __str__(self):
        return "{}".format(self.id)
