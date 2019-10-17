from django.db import models


class AbstractComment(models.Model):
    """Абстрактная модель комментариев"""
    text = models.TextField("Сообщение", max_length=2000)
    created_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    update_date = models.DateTimeField("Изменен", auto_now=True)
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        abstract = True
