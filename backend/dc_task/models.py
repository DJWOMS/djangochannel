from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db import models


class CategoryTask(MPTTModel):
    """Модель категорий заданий"""
    title = models.CharField("Название", max_length=200, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField(max_length=200, unique=True)
    mastery_need = models.FloatField("Требуется мастерства", default=0)
    points_need = models.FloatField("Требуется балов", default=0)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = "Категория задания"
        verbose_name_plural = "Категории заданий"


class DCTask(models.Model):
    """Модель заданий"""
    category = models.ForeignKey(CategoryTask, verbose_name="Категория", on_delete=models.CASCADE)
    mastery_need = models.FloatField("Требуется мастерства", default=0)
    points_need = models.FloatField("Требуется балов", default=0)
    mastery = models.FloatField("Получит мастерства", default=0)
    points = models.FloatField("Получит балов", default=0)
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    slug = models.SlugField(max_length=200, unique=True)
    users = models.ManyToManyField(User, verbose_name="Взявшие", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class AnswerDCTask(models.Model):
    """Выполненые задания"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    task = models.ForeignKey(DCTask, verbose_name="Задание", on_delete=models.CASCADE)
    answer = models.TextField("Ответ")
    result = models.BooleanField("Сдано?", default=False)
    check = models.BooleanField("На проверке", default=False)
    verifiers_y = models.ManyToManyField(
        User,
        verbose_name="Проверяюще за",
        related_name="users_check_y",
        blank=True
    )
    verifiers_n = models.ManyToManyField(
        User,
        verbose_name="Проверяюще против",
        related_name="users_check_n",
        blank=True
    )
    count_check = models.IntegerField("Общее за", default=0)
    mentor = models.ForeignKey(
        User,
        verbose_name="Ментор",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_mentor"
    )
    created = models.DateTimeField("Взято", auto_now_add=True)
    over = models.DateTimeField("Сдано", blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.task)

    class Meta:
        verbose_name = "Взятое задание"
        verbose_name_plural = "Взятые задания"


class Skills(models.Model):
    """Навыки пользователя"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    skill = models.ForeignKey(
        CategoryTask,
        verbose_name="Специализация / Навык",
        on_delete=models.CASCADE,
        related_name="skill_user")
    points = models.FloatField("Балы", default=0)

    def all_skills(self):
        return Skills.objects.filter(user=self.user)

    def __str__(self):
        return "{} - {}".format(self.user, self.skill)

    class Meta:
        verbose_name = "Навык пользователя"
        verbose_name_plural = "Навыки пользователя"
