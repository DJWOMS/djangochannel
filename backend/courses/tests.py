# from django.test import TestCase
# from django.contrib.auth.models import User
# from django.test import Client
#
# # Create your tests here.
#
# from .models import Course, RealizationTask, Category
# from .views import AllCourses
#
#
# #
# #
# # class OpenedTasks:
# #     def get(self, request):
# #         course_pk = request.GET.get('course_pk')
# #         course = Course.objects.get(id=course_pk)
# #         tasks = course.tasks.all()
# #         completed_tasks = RealizationTask.objects.filter(
# #             student=request.user, success=True, task__in=tasks)
# #         c
#
#
# class CourseTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         user = User.objects.create(username="Hamel")
#         category = Category.objects.create(title="Категория", slug="test_slug")
#
#         course = Course.objects.create(
#                               title="Test course",
#                               slug="slug",
#                               description="Описание",
#                               program="Программа курса",
#                               target_audience="Целевая аудитория",
#                               category=category,
#                               requirements="Требования",
#                               desc_for_student="Описание для студентов",
#                               price=10000,
#                               date_start="2019-05-25",
#                               date_end="2019-06-25",
#                               count_tasks=25,
#                               available=50,
#                               is_active=True,
#                               # is_complete=False,
#                               lessons_on_weak=5,
#                               lessons_time="15:00",
#                               # buy_link=""
#                               instructor=user,
#                               )
#         st = course.students
#         st.add(user)
#
#     def test_course(self):
#         course = Course.objects.get(title="Test course")
#         self.assertEqual(course.available, 50)
#
#     def test_course2(self):
#         course = Course.objects.get(program="Программа курса")
#         self.assertEqual(course.price, 10000)
#
#     def test_course3(self):
#         course = Course.objects.get(slug="slug")
#         self.assertEqual(course.is_active, True)
#
#     def test_all_courses(self):
#         response = self.client.get("")
#         self.assertEqual(response.status_code, 200)
#
#     def test_list_course(self):
#         response = self.client.get("", {"slug": "test_slug"})
#         self.assertEqual(response.status_code, 200)
#
#     def test_course_detail(self):
#         response = self.client.get("", {"slug": "category"}, {"slug": "test_slug"})
#         self.assertEqual(response.status_code, 200)
#
