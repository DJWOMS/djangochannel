from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SimpleRight(models.Model):
    """Отдельное право модератора"""
    description = models.CharField('Описание', max_length=50)
    key = models.PositiveIntegerField('Числовое значение', unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Право'
        verbose_name_plural = 'Права'


class ModeratorRights(models.Model):
    """Права модератора"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Модератор',
        related_name='moderator_rights'
    )
    rights = models.ManyToManyField(
        SimpleRight,
        verbose_name='Права'
    )

    # class Meta:
    #     verbose_name = 'Право модератора'
    #     verbose_name_plural = 'Права модераторов'

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Права модератора'
        verbose_name_plural = 'Права модераторов'


class BannedUser(models.Model):
    """Модель бана пользователя"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='bans'
    )
    ban_action = models.IntegerField(verbose_name='Действие')
    moderator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Модератор',
        related_name='mod_bans'
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Бан пользователя'
        verbose_name_plural = 'Баны пользователей'
