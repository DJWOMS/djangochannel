import os

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

User = settings.AUTH_USER_MODEL


def get_path_upload_image(group, user, file):
    """
    make path of uploaded file shorter and return it
    in following format: (media)/profile_pics/user_1/myphoto_2018-12-2.png
    """
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + time + '.' + end_extention
    return os.path.join('{0}/', 'user_{1}_{2}').format(group, user, file_name)


class Groups(models.Model):
    """Модель сообществ и групп"""

    group_variety_choices = (
        ("open", "Открытая"),
        ("closed", "Закрытая"),
        ("private", "Приватная"),
        ("team", "Команда"),
    )

    title = models.CharField("Название", max_length=50)
    group_variety = models.CharField("Вид группы",
                                     max_length=10,
                                     choices=group_variety_choices,
                                     default="open")
    founder = models.ForeignKey(
        User,
        verbose_name="Основатель",
        related_name="creator",
        on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User,
        blank=True,
        related_name="partner",
        verbose_name="Участники")
    desc = models.TextField("Описание", max_length=1000)
    image = models.ImageField("Изображение", upload_to="groups/image/", blank=True)
    miniature = models.ImageField("Миниатюра", upload_to="groups/miniature/", blank=True)

    class Meta:
        verbose_name = "Группа и команда"
        verbose_name_plural = "Группы и команды"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = get_path_upload_image(self.title, self.founder_id, self.image.name)
            self.miniature.name = get_path_upload_image(self.title, self.founder_id, self.miniature.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail_groups", kwargs={"pk": self.id})


class EntryGroup(models.Model):
    """Записи в группе"""
    title = models.CharField("Заголовок записи", max_length=50, default="")
    group = models.ForeignKey(
        Groups,
        related_name='entry',
        verbose_name="Группа",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
    text = models.TextField("Текст записи", max_length=5000)
    created_date = models.DateTimeField("Дата добавления", auto_now_add=True, null=False)
    
    class Meta:
        verbose_name = "Запись группы"
        verbose_name_plural = "Записи группы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_groups", kwargs={"pk": self.group_id})


class GroupLink(models.Model):
    """Ссылки группы"""
    title = models.CharField("Заголовок", max_length=250, blank=True)
    group = models.ForeignKey(
        Groups,
        verbose_name="Группа",
        on_delete=models.CASCADE
    )
    link = models.URLField("URL")

    class Meta:
        verbose_name = "Ссылка группы"
        verbose_name_plural = "Ссылки группы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_groups", kwargs={"pk": self.group_id})
