import os
from PIL import Image

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField

from backend.courses.models import Course
from backend.moderation.models import ModeratorRights
from backend.utils.models import AbstractImageModel

# from backend.utils.send_mail import send_mail_edit_password


def get_path_upload_avatar(instance, file):
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
    return os.path.join('profile_cover', 'user_{0},{1}').format(instance.user.id, file_name)


class UserProfile(AbstractImageModel):
    """Модель профиля пользователя"""

    # TODO: Непонятно зачем сдесь username и email, нужно исправить

    description = 'Профиль'

    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        related_name='profile',
        on_delete=models.CASCADE
    )
    completed_courses = models.ManyToManyField(
        Course,
        blank=True,
        verbose_name='Пройденные курсы'
    )
    # friends = models.ManyToManyField(User, verbose_name="Дрезья", blank=True)
    name = models.CharField(max_length=50, editable=False)
    email = models.EmailField(editable=False)
    is_forum_moderator = models.BooleanField('Модератор', default=False)
    mastery = models.FloatField("Мастерство", default=0)
    cover = models.ImageField(
        'Обложка',
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True
    )
    public = models.BooleanField("Публичный профиль", default=True)

    class Meta:
        verbose_name = 'Профиль пользователь'
        verbose_name_plural = 'Профили пользователей'

    def image_tag(self):
        return mark_safe('<img src="{}" />'.format(self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.get_username()

    def save(self, *args, **kwargs):
        # super(UserProfile, self).save(*args, **kwargs)
        if not self.name:
            self.name = self.get_username()
        if not self.email or self.email != self.user.email:
            self.email = self.get_email()

        if self.is_forum_moderator:
            if not ModeratorRights.objects.filter(user=self.user).exists():
                ModeratorRights.objects.create(user=self.user)

        # img = Image.open(self.cover.path)
        # if img.height > 300:
        #     output_size = (img.width, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.cover.path)

        super().save(*args, **kwargs)

    def count_course(self):
        return self.completed_courses.count()

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def get_completed_courses(self):
        return self.completed_courses

    # def get_info(self):
    #     return {'username': self.username,
    #             'email': self.email,
    #             'avatar': self.image or None,
    #             'courses': self.get_completed_courses()}


class PersonalRecords(models.Model):
    """Модель личного дневника пользователя"""

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name='diary',
        on_delete=models.CASCADE)
    title = models.CharField("Заголовок заметки", max_length=50, default="")
    note = RichTextField("Текст заметки", max_length=1000, config_name='special')
    for_all = models.BooleanField("Публично?", default=False)
    date = models.DateField("Дата создания", auto_now=True)
    update = models.DateField("Дата редактирования", blank=True, null=True)

    class Meta:
        verbose_name = 'Личный дневник пользователь'
        verbose_name_plural = 'Личные дневники пользователей'
        ordering = ["-date"]

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        UserProfile.objects.create(user=instance, id=instance.id)
        instance.profile.save()

# @receiver(post_save, sender=User)
# def create_user_post(sender, instance, created, **kwargs):
#     """Отправка email о смене пароля пользователя"""
#     if created:
#         send_mail_edit_password(instance)
