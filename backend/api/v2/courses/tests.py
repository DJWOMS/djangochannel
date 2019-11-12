import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from backend.courses.models import Category, Course
from .serializers import ListCategoryCourseSerializer, DetailCourseSerializer


class CoursesTests(APITestCase):

    def setUp(self):
        self.one_category = Category.objects.create(title="Python", slug="python")
        Category.objects.create(title="Django", slug="django")

        self.one_course = Course.objects.create(
            title="Course Python",
            slug="c_python",
            category=self.one_category,
            description="Test",
            price=0,
            date_start="2019-10-14",
            date_end="2019-11-14",
            is_active=True,
            is_complete=False
        )

        self.two_course = Course.objects.create(
            title="Course Django",
            slug="d_python",
            category=self.one_category,
            description="Test",
            price=500,
            date_start="2019-10-17",
            date_end="2019-11-18",
            is_active=True,
            is_complete=False
        )

        user_test1 = User.objects.create_user(username='test', password="1q2w3e")
        user_test1.save()
        self.user_test1_token = Token.objects.create(user=user_test1)

    def test_category_list(self):
        response = self.client.get(reverse('course_categories'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertTrue({'id': 1, 'title': 'Python', 'slug': 'python'} in response.json().get("results"))

    def test_detail_course_db(self):
        course = Course.objects.get(id=self.one_course.id)
        self.assertEqual(course.title, "Course Python")

    def test_detail_course(self):
        response = self.client.get(reverse('detail_course', kwargs={"pk": self.one_course.id}))
        serializer_data = DetailCourseSerializer(self.one_course).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_enter_invalid_course(self):
        response = self.client.post(
            reverse('detail_course', kwargs={"pk": self.one_course.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_enter_valid_course(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.post(
            reverse('detail_course', kwargs={"pk": self.one_course.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_enter_valid_course_pay(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.post(
            reverse('detail_course', kwargs={"pk": self.two_course.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)