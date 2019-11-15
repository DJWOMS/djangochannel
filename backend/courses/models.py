from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

from backend.utils.models import AbstractImageModel
from backend.dc_tests.models import Test
from backend.utils.send_mail import send_mail_mess_student
User = settings.AUTH_USER_MODEL


class Category(AbstractImageModel):
    """Модель категорий"""
    title = models.CharField('Категория', max_length=50)
    slug = models.CharField(max_length=100, default="category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(AbstractImageModel):
    """Класс модели курсов"""
    title = models.CharField('Название курса', max_length=100)
    slug = models.SlugField(max_length=100, default="", unique=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='courses',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    description = RichTextUploadingField('Описание курса', max_length=5000)
    program = RichTextUploadingField('Программа курса', max_length=5000, null=True)
    target_audience = RichTextUploadingField('Целевая аудитория', max_length=5000, null=True)
    requirements = RichTextUploadingField('Требования', max_length=5000, null=True)
    desc_for_student = RichTextUploadingField('Описание для студентов', blank=True, null=True)
    price = models.IntegerField('Стоимость курса')
    date_start = models.DateField('Дата начала курса')
    date_end = models.DateField('Дата окончания курса')
    students = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='Учащиеся',
        related_name='courses'
    )
    instructor = models.ForeignKey(
        User,
        verbose_name='Преподаватель',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='my_courses'
    )
    count_tasks = models.PositiveIntegerField('Количество заданий', default=0)
    available = models.IntegerField('Количество мест', default=0)
    is_active = models.BooleanField('Активный', default=False)
    is_complete = models.BooleanField("Запись завершена", default=False)
    lessons_on_weak = models.PositiveIntegerField('Количество занятий в неделю', default=0)
    lessons_time = models.CharField('Время проведения занятий', max_length=500, null=True, blank=True)
    buy_link = models.CharField("Ссылка на оплату", max_length=1000, blank=True, null=True)
    test_in_course = models.ForeignKey(
        Test,
        verbose_name="Тест для поступления",
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses_detail', kwargs={"category": self.category.slug, "slug": self.slug})

    def term(self):
        return self.date_end - self.date_start
    term.short_description = 'Длительность курса'

    def count_seats(self):
        return self.available - self.students.count()
    count_seats.short_description = 'Свободно мест'

    def count_students(self):
        return self.students.count()
    count_students.short_description = 'Количество учеников'

    def course_complete(self):
        """Сравнение на заполненность курса"""
        if self.students.count() == self.available:
            self.is_complete = True
            return self.is_complete

    def tasks_all(self):
        return Task.objects.filter(course_id=self.id).order_by("title")

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Task(models.Model):
    """Класс модели задания курса"""
    course = models.ForeignKey(
        Course,
        verbose_name='Курс',
        related_name='tasks',
        on_delete=models.CASCADE)
    title = models.CharField('Название задания', max_length=50)
    description = RichTextUploadingField('Описание задания', max_length=3000)
    date_start = models.DateTimeField('Дата начала выполнения задания')
    date_end = models.DateTimeField('Дата окончания выполнения задания')
    # questions = models.ManyToManyField(
    #     Question,
    #     verbose_name='Задания',
    #     related_name='tasks',
    #     blank=True
    # )
    test = models.ForeignKey(
        Test,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Тест',
        related_name='tasks'
    )
    active = models.BooleanField("Вывести задание", default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ["title"]

    def __str__(self):
        return self.title


@receiver(post_save, sender=Task)
def plus_count_tasks(instance, created, **kwargs):
    """Прибавление 1 к счетчику заданий в курсе"""
    if created:
        instance.course.count_tasks += 1
        instance.course.save()


@receiver(post_delete, sender=Task)
def minus_count_tasks(instance, **kwargs):
    """Убавление 1 от счетчика заданий в курсе"""
    instance.course.count_tasks -= 1
    instance.course.save()


class RealizationTask(models.Model):
    """Модель исполнения задания"""
    #TODO После курса нужно убрать поля - answer, comment
    task = models.ForeignKey(
        Task,
        verbose_name='Выполнение',
        on_delete=models.CASCADE,
        related_name='answers'
    )
    student = models.ForeignKey(User, verbose_name='Ученик', on_delete=models.CASCADE)
    answer = RichTextUploadingField('Ответ', max_length=1000, config_name='course')
    comment = RichTextUploadingField('Комментарий преподавателя', max_length=1500, blank=True)
    success = models.BooleanField('Выполнено', default=False)
    date_create = models.DateTimeField('Дата сдачи', auto_now_add=True)

    def __str__(self):
        return self.task.title

    def add_course_in_completed(self):
        realizations_count = RealizationTask.objects.filter(student=self.student).count()
        tasks_count = self.task.course.count_tasks
        if realizations_count == tasks_count:
            self.student.profile.completed_courses.add(self.task.course)

    def save(self, *args, **kwargs):
        self.add_course_in_completed()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Выполненное задание'
        verbose_name_plural = 'Выполненные задания'


class MessagesTask(models.Model):
    """Сообщения в задании"""
    realiz_task = models.ForeignKey(
        RealizationTask,
        verbose_name='Выполнение',
        on_delete=models.CASCADE,
        related_name='realiz_task'
    )
    user = models.ForeignKey(User, verbose_name='Отправитель', on_delete=models.CASCADE)
    answer = RichTextUploadingField('Сообщение', max_length=10000, config_name='course')
    created = models.DateTimeField("Дата", auto_now_add=True)
    read = models.BooleanField("Просмотренно", default=False)

    def __str__(self):
        return "{}".format(self.realiz_task)

    class Meta:
        verbose_name = "Сообщение в задании"
        verbose_name_plural = "Сообщения в задании"


class MessageForStudent(models.Model):
    """Сообщение для участников курса"""
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE)
    subject = models.CharField("Тема", max_length=200)
    message = RichTextUploadingField("Сообщение")
    send = models.BooleanField("Отправить сразу?", default=False)
    date = models.DateField("Дата", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.course, self.subject)

    class Meta:
        verbose_name = "Сообщение участникам курса"
        verbose_name_plural = "Сообщения участникам курса"


class CheckPAyUser(models.Model):
    """Пользователи которые должны оплатить курс"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE)
    summ = models.PositiveIntegerField("Сумма к оплате", default=0)
    date = models.DateTimeField("Дата", auto_now_add=True)
    status = models.BooleanField("Статус", default=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.course)

    class Meta:
        verbose_name = "Ожидание оплаты"
        verbose_name_plural = "Ожидание оплаты"


@receiver(post_save, sender=MessageForStudent)
def mess_student(instance, created, **kwargs):
    """Оповищение студентов по email"""
    if instance.send:
        send_mail_mess_student(
            [user.email for user in instance.course.students.all()],
            instance.subject,
            instance.message)
