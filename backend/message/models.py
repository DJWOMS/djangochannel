from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from backend.utils.send_mail import send_mail_new_mess


class Room(models.Model):
    """Чат комната"""
    creator = models.ForeignKey(User, verbose_name="Отправитель", on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        User,
        verbose_name="Получатель",
        on_delete=models.CASCADE,
        related_name="user_recipient")

    def mess_no_read_count(self):
        return PrivatMessages.objects.filter(read=False).exclude(user=self.request.user).count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_mail_new_mess(self.creator, self.recipient.email)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class PrivatMessages(models.Model):
    """Модель личных сообщений"""
    user = models.ForeignKey(
        User, verbose_name="Отправитель", on_delete=models.CASCADE, related_name="private_mess_user"
    )
    room = models.ForeignKey(Room, verbose_name="Чат", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=20000)
    created = models.DateTimeField("Дата", auto_now_add=True)
    read = models.BooleanField("Просмотренно", default=False)

    def __str__(self):
        return "{}".format(self.room)

    class Meta:
        verbose_name = "Личное сообщение"
        verbose_name_plural = "Личные сообщения"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     send_mail_new_mess(self.room.creator, self.user.email)


