from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Category, Course, Task, RealizationTask
from .serializers import (
    CategorySerializer,
    MinimalCourseSerializer, CourseSerializer, OutputCourseSer, ImageCourseSerializer,
    MinimalTaskSerializer, FullTaskSerializer,
    MinRealizationTaskSerializer, RealizationTaskSerializer, PatchRealizationTaskSerializer
)


class CategoryList(APIView):
    """Список всех категорий"""
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get(request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response({'categories': serializer.data})


class CoursesInCategory(APIView):
    """Список курсов в категории"""
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get(request):
        pk = request.GET.get('pk', None)

        if not pk:
            return Response('Нет pk', status=400)

        try:
            courses = Course.objects.filter(category_id=pk, is_active=True)
        except ObjectDoesNotExist:
            return Response('Нет категории', status=404)

        serializer = ImageCourseSerializer(courses, many=True)
        return Response({'courses': serializer.data})


class MyCourses(APIView):
    """Список курсов текущего юзера"""
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        courses = Course.objects.filter(students=request.user)
        serializer = MinimalCourseSerializer(courses, many=True)
        return Response({'courses': serializer.data})


class CourseTasks(APIView):
    """Задания курса"""
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        pk = request.GET.get('pk', None)

        if not pk:
            return Response('Нет pk', status=400)

        try:
            course = Course.objects.get(id=pk)

            if request.user not in course.students.all():
                return Response('Вы не записаны на этот курс', status=403)

            course_ser = CourseSerializer(course)
        except ObjectDoesNotExist:
            return Response('Нет курса', status=404)

        tasks = course.tasks.all()
        tasks_ser = MinimalTaskSerializer(tasks, many=True)

        confirmed, unconfirmed, next_task, status = CompletedTasks().get(request, course_pk=pk)

        # Возможные статусы:
        # 200 - все ок,
        # 400 - нет pk курса,
        # 403 - юзер не записан на курс,
        # 404 - нет курса.

        if status != 200:
            return Response(status=status)

        return Response({'course': course_ser.data,
                         'tasks': tasks_ser.data,
                         'confirmed': confirmed,
                         'unconfirmed': unconfirmed,
                         'next': next_task})


class CourseDescription(APIView):
    """Описание курса"""
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get(request):
        pk = request.GET.get('pk', None)

        if not pk:
            return Response('Нет pk', status=400)

        try:
            course = Course.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response('Нет курса', status=404)

        serializer = OutputCourseSer(course)
        return Response({'course': serializer.data})


class Tasks(APIView):
    """
    Получение описания задания
    и его выполнение/изменение
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Получение описания задания"""
        pk = request.GET.get('pk', None)

        if not pk:
            return Response('Нет pk', status=400)

        if self.check_user(request, pk) is False:
            return Response('Это задание недоступно', status=404)

        try:
            task = Task.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response('Нет задания', status=404)

        if request.user not in task.course.students.all():
            return Response('Вы не записаны на этот курс', status=403)

        answer = self.get_realization_task(task, request.user)

        task_serializer = FullTaskSerializer(task)

        return Response({'task': task_serializer.data,
                         'realization': answer})

    @staticmethod
    def get_realization_task(task, user):
        """Получение ответа на задание"""
        try:
            answer = task.answers.get(student=user)
            return RealizationTaskSerializer(answer).data
        except ObjectDoesNotExist:
            return {}

    def post(self, request):
        """Выполнение задания/изменение ответа"""
        task_id = request.data.get('task')

        if self.check_user(request, task_id) is False:
            return Response('Не жульничай', status=404)

        try:
            answer = RealizationTask.objects.get(id=request.data.get("id"))
            serializer = PatchRealizationTaskSerializer(answer, data=request.data)
        except:
            serializer = MinRealizationTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user)
        else:
            return Response(serializer.errors, status=400)
        return Response(status=200)

    @staticmethod
    def check_user(request, task_id):
        """
        Проверка юзера на жульничество,
        выполнение недоступных заданий
        """
        try:
            course = Task.objects.get(id=task_id).course
        except ObjectDoesNotExist:
            return False

        next_task = CompletedTasks().get_next_task(request, course_pk=course.id)

        if next_task is not None and next_task.id < int(task_id):
            return False
        return True


class BuyCourse(APIView):
    """Покупка курса"""
    # TODO: Пока сделано без каких-либо финансовых манипуляций, просто запись на курс
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        pk = request.data.get('pk', None)

        if not pk:
            return Response('Нет pk', status=400)

        try:
            course = Course.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response('Нет курса', status=404)

        if request.user in course.students.all():
            return Response('Вы уже записаны на курс {}'.format(course.title), status=422)

        course.students.add(request.user)
        return Response('Вы записались на курс {}'.format(course.title))


class CompletedTasks:
    """
    Получение подтвержденных,
    неподтвержденных и следующего на выполнение заданий
    """

    def __init__(self):
        self.confirmed_tasks = []
        self.unconfirmed_tasks = []
        self.next_task = None

    def get(self, request, **kwargs):
        # Получение pk, проверка на его наличие
        course_pk = request.GET.get('course_pk')
        if not course_pk:
            course_pk = kwargs.get('course_pk')
        if not course_pk:
            return [], [], None, 400

        # Получение курса
        try:
            course = Course.objects.get(id=course_pk)
        except ObjectDoesNotExist:
            return [], [], None, 404

        # Проверка на наличие юзера в учениках курса
        if request.user not in course.students.all():
            return [], [], None, 403

        # Получение подтвержденных заданий
        self.confirmed_tasks = self.get_tasks(course, request.user, True)
        ser_confirmed_data = MinimalTaskSerializer(self.confirmed_tasks, many=True).data

        # Получение неподтвержденных заданий
        self.unconfirmed_tasks = self.get_tasks(course, request.user, False)
        ser_unconfirmed_data = MinimalTaskSerializer(self.unconfirmed_tasks, many=True).data

        # Получение следующего для выполнения задания
        self.next_task = Task.objects.filter(
            course=course
        ).exclude(
            id__in=[x.id for x in self.confirmed_tasks]
        ).first()
        next_task_data = MinimalTaskSerializer(self.next_task).data if self.next_task else None

        return ser_confirmed_data, ser_unconfirmed_data, next_task_data, 200

    @staticmethod
    def get_tasks(course, user, success):
        # TODO: Изменить запрос на более правильный
        answers = RealizationTask.objects.filter(
            task__course=course, student=user, success=success)
        return [x.task for x in answers]

    def get_next_task(self, request, **kwargs):
        self.get(request, **kwargs)
        return self.next_task
