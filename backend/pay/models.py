from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from backend.courses.models import Course


class Pay(models.Model):
    """Модель сделанных заказов"""
    account = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    item = models.ForeignKey(Course, verbose_name='Купленный курс', on_delete=models.CASCADE)
    status = models.BooleanField('Статус платежа', default=False)
    date_create = models.DateTimeField('Дата создания', default=timezone.now)
    date_complete = models.DateTimeField('Дата оплаты', blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return str(self.item)
