import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, DetailView, ListView, CreateView

from DS import settings
from backend.contact.forms import ContactForm

from .models import (Course, Task, RealizationTask, MessagesTask, CheckPAyUser)
from .forms import AnswerTaskForm
#from .tasks import check_api #CheckPay


logging.basicConfig(
    filename='log/pay.log',
    format="%(levelname)-10s %(lineno)d %(asctime)s %(message)s",
    level=logging.INFO
)

log = logging.getLogger('pay')


class AllCourses(ListView):
    """Список всех курсов"""
    model = Course
    queryset = Course.objects.filter(is_active=True)
    template_name = "courses/course-list.html"


class ListCourse(ListView):
    """Список курсов по категории"""
    template_name = "courses/course-list.html"

    def get_queryset(self):
        return Course.objects.filter(category__slug=self.kwargs.get("slug"), is_active=True)


class CourseDetail(DetailView):
    """Вывод информации о курсе"""
    model = Course
    context_object_name = "course"
    template_name = "courses/course-detail.html"

    def check(self):
        if self.request.user.is_authenticated:
            try:
                Course.objects.get(slug=self.kwargs.get("slug"), students=self.request.user)
                return True
            except Course.DoesNotExist:
                try:
                    CheckPAyUser.objects.get(
                        user=self.request.user,
                        course__slug=self.kwargs.get("slug"),
                        status=False)
                    return False
                except CheckPAyUser.DoesNotExist:
                    return None
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        context["check"] = self.check()
        return context

    def post(self, request, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(self.request, settings.MY_INFO,
                                 'Спасибо, Ваше сообщение отправлено, ответ придет на указанный email')
        return HttpResponseRedirect(request.path)


class MyCourses(LoginRequiredMixin, ListView):
    """Список курсов текущего юзера"""
    model = Course
    template_name = "courses/list-my-courses.html"

    def get_queryset(self):
        return Course.objects.filter(students=self.request.user)


class MyCourseDetail(View):
    """Подробнее о курсе на который записан пользователь"""
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)

        if request.user not in course.students.all():
            raise Http404
        return render(request, "courses/my-course-detail.html", {"course": course})


class TaskCourse(View):
    """Задание курса"""
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk, active=True)
        if self.check_user(request, pk) is False:
            raise Http404
        if request.user not in task.course.students.all():
            raise Http404
        answer = self.get_realization_task(task, request.user)
        context = {"task": task, "answer": answer, "course": task.course, "form": AnswerTaskForm()}
        return render(request, "courses/task-course.html", context)

    @staticmethod
    def get_realization_task(task, user):
        """Получение ответа на задание"""
        try:
            # return MessagesTask.objects.filter(realiz_task=task.answers.get(student=user))
            return MessagesTask.objects.filter(realiz_task=RealizationTask.objects.get(task=task,
                                                                                       student=user))
        except ObjectDoesNotExist:
            return {}

    def post(self, request, pk):
        """Выполнение задания/изменение ответа"""
        # task_id = request.data.get('task')

        if self.check_user(request, pk) is False:
            messages.add_message(self.request, settings.TASK_MESS, 'Не жульничай')
            return HttpResponseRedirect(request.path)

        try:
            answer = RealizationTask.objects.get(task_id=pk, student=request.user)
            # form = AnswerTaskForm(data=request.POST, instance=answer)
        except:
            answer = RealizationTask.objects.create(task_id=pk, student=request.user)
        form = AnswerTaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.realiz_task = answer
            form.user = request.user
            form.save()
            messages.add_message(self.request, settings.TASK_MESS, 'Ответ отправлен')
        else:
            messages.add_message(self.request, settings.TASK_MESS, 'Ошибка сохранения')
        return HttpResponseRedirect(request.path)

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

        # next_task = CompletedTasks().get_next_task(request, course_pk=course.id)
        #
        # if next_task is not None and next_task.id < int(task_id):
        #     return False
        # return True


class SetUserCoursePay(View):
    """Запись пользователя на ожидание оплаты"""
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        check = CheckPAyUser.objects.get_or_create(
            user=request.user,
            course=course)
        #check_api.delay(request.user.id, request.user.username)
        return redirect("{}".format(check[0].course.buy_link))

    def post(self, request):
        course = Course.objects.get(test_in_course_id=request.POST.get("test_pk"))
        check = CheckPAyUser.objects.get_or_create(
            user=request.user,
            course=course,
            summ=course.price)
        #check_api.delay(request.user.id, request.user.username)
        return HttpResponse(status=201)


# class CompletedTasks:
#     """
#     Получение подтвержденных,
#     неподтвержденных и следующего на выполнение заданий
#     """
#
#     def __init__(self):
#         self.confirmed_tasks = []
#         self.unconfirmed_tasks = []
#         self.next_task = None
#
#     def get(self, request, **kwargs):
#         # Получение pk, проверка на его наличие
#         course_pk = request.GET.get('course_pk')
#         if not course_pk:
#             course_pk = kwargs.get('course_pk')
#         if not course_pk:
#             return [], [], None, 400
#
#         # Получение курса
#         try:
#             course = Course.objects.get(id=course_pk)
#         except ObjectDoesNotExist:
#             return [], [], None, 404
#
#         # Проверка на наличие юзера в учениках курса
#         if request.user not in course.students.all():
#             return [], [], None, 403
#
#         # Получение подтвержденных заданий
#         self.confirmed_tasks = self.get_tasks(course, request.user, True)
#         ser_confirmed_data = MinimalTaskSerializer(self.confirmed_tasks, many=True).data
#
#         # Получение неподтвержденных заданий
#         self.unconfirmed_tasks = self.get_tasks(course, request.user, False)
#         ser_unconfirmed_data = MinimalTaskSerializer(self.unconfirmed_tasks, many=True).data
#
#         # Получение следующего для выполнения задания
#         self.next_task = Task.objects.filter(
#             course=course
#         ).exclude(
#             id__in=[x.id for x in self.confirmed_tasks]
#         ).first()
#         next_task_data = MinimalTaskSerializer(self.next_task).data if self.next_task else None
#
#         return ser_confirmed_data, ser_unconfirmed_data, next_task_data, 200
#
#     @staticmethod
#     def get_tasks(course, user, success):
#         # TODO: Изменить запрос на более правильный
#         answers = RealizationTask.objects.filter(
#             task__course=course, student=user, success=success)
#         return [x.task for x in answers]
#
#     def get_next_task(self, request, **kwargs):
#         self.get(request, **kwargs)
#         return self.next_task



