from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.utils.send_mail import send_mail_contact


class Contact(models.Model):
    """Модель обратной связи"""
    email = models.EmailField("Email")
    title = models.CharField("Тема", max_length=200)
    message = models.TextField("Сообщение")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.title


@receiver(post_save, sender=Contact)
def create_contact(sender, instance, created, **kwargs):
    """Отправка сообщения о создании новой темы на email"""
    if created:
        send_mail_contact(instance)
