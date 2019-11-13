import os
from django.core.exceptions import ValidationError as DjangoValidationError

from PIL import Image
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from backend.comments.models import AbstractComment

User = settings.AUTH_USER_MODEL


def get_path_upload_image(group, user, file):
    """
    make path of uploaded file shorter and return it
    in following format: (media)/profile_pics/user_1/myphoto_2018-12-2.png
    """
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split(".")[-1]
    head = file.split(".")[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + "_" + time + "." + end_extention
    return os.path.join("{0}/", "user_{1}_{2}").format(group, user, file_name)


class Groups(models.Model):
    """Модель сообществ и групп"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image_min_h = kwargs.get('min_height', 1152)
        self.image_min_w = kwargs.get('min_width', 2048)
        self.image_max_h = kwargs.get('max_height', 1440)
        self.image_max_w = kwargs.get('max_width', 2560)

        self.thumb_min_h = kwargs.get('min_height', 50)
        self.thumb_min_w = kwargs.get('min_width', 50)
        self.thumb_max_h = kwargs.get('max_height', 150)
        self.thumb_max_w = kwargs.get('max_width', 150)

    image_height = models.IntegerField(editable=False, null=True)
    image_width = models.IntegerField(editable=False, null=True)

    thumb_height = models.IntegerField(editable=False, null=True)
    thumb_width = models.IntegerField(editable=False, null=True)

    group_variety_choices = (
        ("open", "Открытая"),
        ("closed", "Закрытая"),
        ("private", "Приватная"),
        ("team", "Команда"),
    )

    title = models.CharField("Название", max_length=50)
    group_variety = models.CharField(
        "Вид группы", max_length=10, choices=group_variety_choices, default="open"
    )
    founder = models.ForeignKey(
        User,
        verbose_name="Основатель",
        related_name="creator",
        on_delete=models.CASCADE,
    )
    members = models.ManyToManyField(
        User, blank=True, related_name="partner", verbose_name="Участники"
    )
    desc = models.TextField("Описание", max_length=1000)
    image = models.ImageField(
        "Изображение",
        upload_to="groups/image/",
        height_field='image_height',
        width_field='image_width',
    )
    miniature = models.ImageField(
        "Миниатюра",
        upload_to="groups/miniature/",
        height_field='thumb_height',
        width_field='thumb_width',
    )

    class Meta:
        verbose_name = "Группа и команда"
        verbose_name_plural = "Группы и команды"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.check_size_thumb() and self.check_size_image():
            self.image.name = get_path_upload_image(
                self.title, self.founder_id, self.image.name
            )

            self.miniature.name = get_path_upload_image(
                self.title, self.founder_id, self.miniature.name
            )
            super().save(*args, **kwargs)
            self.work_image()
        else:
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail_groups", kwargs={"pk": self.id})

    def work_image(self):
        """Сжатие изображения и создание миниатюры"""
        if self.image:
            im = Image.open(self.image.path)
            im.save(self.image.path, 'JPEG', optimize=True, quality=60)
        if self.miniature:
            size = 100, 100
            im = Image.open(self.miniature.path)
            im.thumbnail(size)
            im.save(self.miniature.path, "JPEG")

    def check_size_thumb(self):
        """Проверка размера миниатюр"""
        if self.miniature and self.thumb_height >= self.thumb_min_h and self.thumb_width >= self.thumb_min_w \
                and self.thumb_height <= self.thumb_max_h and self.thumb_width <= self.thumb_max_w:
            return True
        else:
            return False

    def check_size_image(self):
        """Проверка размера изображения"""
        if self.image and self.image_height >= self.image_min_h and self.image_width >= self.image_min_w \
                and self.image_height <= self.image_max_h and self.image_width <= self.image_max_w:
            return True
        else:
            return False

    def full_clean(self, *args, **kwargs):
        """ Добавлена логика проверки размеров
        изображения при добавлении через админку
        """
        super().full_clean(*args, **kwargs)

        if not self.check_size_image():
            raise DjangoValidationError(f'Размер изображения должен быть не менее {self.image_min_h}'
                                        f'x{self.image_min_w} пикселей')
        if not self.check_size_thumb():
            raise DjangoValidationError(f'Размер миниатюры должен быть не менее {self.thumb_min_h}'
                                        f'x{self.thumb_min_w} пикселей')


class EntryGroup(models.Model):
    """Записи в группе"""

    title = models.CharField("Заголовок записи", max_length=50, default="")
    group = models.ForeignKey(
        Groups, related_name="entry", verbose_name="Группа", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField("Текст записи", max_length=5000)
    created_date = models.DateTimeField(
        "Дата добавления", auto_now_add=True, null=False
    )

    class Meta:
        verbose_name = "Запись группы"
        verbose_name_plural = "Записи группы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_groups", kwargs={"pk": self.group_id})

    def comments_count(self):
        return self.comment.count()


class CommentEntryGroup(AbstractComment, MPTTModel):
    """Коментарии к записям в группе"""

    entry = models.ForeignKey(
        EntryGroup,
        related_name="comment",
        verbose_name="Запись",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        verbose_name="Родительский комментарий",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    def __str__(self):
        return f"{self.author} - {self.entry}"


class GroupLink(models.Model):
    """Ссылки группы"""

    title = models.CharField("Заголовок", max_length=250, blank=True)
    group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.CASCADE)
    link = models.URLField("URL")

    class Meta:
        verbose_name = "Ссылка группы"
        verbose_name_plural = "Ссылки группы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_groups", kwargs={"pk": self.group_id})
