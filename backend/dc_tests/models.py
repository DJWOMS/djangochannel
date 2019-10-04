from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField

User = settings.AUTH_USER_MODEL

# from courses.models import Course, Task


class TestCategory(models.Model):
    """Модель категорий тестов"""
    title = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Категория тестов'
        verbose_name_plural = 'Категории тестов'

    def __str__(self):
        return self.title


class Test(models.Model):
    """Модель теста"""
    category = models.ForeignKey(
        TestCategory,
        on_delete=models.SET_NULL,
        related_name='tests',
        verbose_name='Категория',
        null=True,
        blank=True
    )
    # course = models.ForeignKey(
    #     Course,
    #     on_delete=models.SET_NULL,
    #     related_name='tests',
    #     verbose_name='Курс',
    #     null=True,
    #     blank=True
    # )
    # task = models.ForeignKey(
    #     Task,
    #     on_delete=models.SET_NULL,
    #     related_name='tests',
    #     verbose_name='Задание',
    #     null=True,
    #     blank=True
    # )

    title = models.CharField('Название', max_length=150)
    active = models.BooleanField("Активный?", default=1)
    in_course = models.BooleanField("Для курса?", default=0)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    """Модель вопроса"""
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Тест'
    )

    text = models.CharField('Вопрос', max_length=150)
    desc = RichTextUploadingField("Описание вопроса", default="")

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        # return self.text
        return self.test_and_question()

    def save(self, *args, **kwargs):
        for x in self.test.counter.all():
            x.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for x in self.test.counter.all():
            x.save()
        super().delete(*args, **kwargs)

    def test_and_question(self):
        return '{} - {}'.format(self.test, self.text)


class PossibleAnswer(models.Model):
    """Модель варианта ответа"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    text = models.CharField('Вариант', max_length=500)
    is_right = models.BooleanField('Является верным ответом', default=False)
    # counter = models.PositiveIntegerField('Счетчик', default=0)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class AnswersCounter(models.Model):
    """Счетчик ответов на вопросы"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answers_counter',
        verbose_name='Пользователь'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='counter',
        verbose_name='Тест'
    )

    questions_count = models.PositiveIntegerField(default=0, editable=False)
    counter = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Ответ на тест"
        verbose_name_plural = "Ответы на тесты"

    def save(self, *args, **kwargs):
        self.questions_count = self.test.questions.all().count()
        # print('questions_count', self.questions_count)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.user, self.test)
