from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from backend.reviews.models import Review
from .serializers import ReviewSerializer


class ProfileTests(APITestCase):

    def setUp(self):
        self.user_test1 = User.objects.create_user(username='test', password="1q2w3e")
        self.user_test1.save()
        self.user_test1_token = Token.objects.create(user=self.user_test1)

        Review.objects.create(
            user=self.user_test1,
            name="TestUser",
            text="Good",
            social_link="https://vk.com/DJWOMS",
            git_link="https://github.com/DJWOMS",
            moderated=True
        )

        self.data = {
            "name": "John",
            "text": "Good teacher",
            "social_link": "https://vk.com/DJWOMS",
            "git_link": "https://github.com/DJWOMS"
        }

    def test_list_reviews(self):
        """Тест вывода списка отзывов"""
        response = self.client.get(reverse('reviews'))
        serializer = ReviewSerializer(Review.objects.filter(moderated=True), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(serializer.data, response.json().get("results"))

    def test_invalid_create_reviews(self):
        """Не авторизованный юзер не может отправить отзыв"""
        response = self.client.post(reverse('reviews'), self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_create_reviews(self):
        """Отправка отзыва авторизованным юзером"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.post(reverse('reviews'), self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
