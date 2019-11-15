from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from backend.profile.models import UserProfile
from .serializers import UserProfilePublicSerializer, UserProfileSerializer


class ProfileTests(APITestCase):

    def setUp(self):
        self.user_test1 = User.objects.create_user(username='test', password="1q2w3e")
        self.user_test1.save()
        self.user_test2 = User.objects.create_user(username='test2', password="1q2w3e2")
        self.user_test2.save()
        self.user_test1_token = Token.objects.create(user=self.user_test1)

    def test_valid_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.get(reverse('profile'))
        serializer = UserProfileSerializer(UserProfile.objects.get(user=self.user_test1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.json())

    def test_invalid_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_public_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.get(reverse('public_profile', kwargs={"pk": self.user_test2.id}))
        serializer = UserProfilePublicSerializer(UserProfile.objects.get(user=self.user_test2))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.json())

    def test_invalid_public_profile(self):
        response = self.client.get(reverse('public_profile', kwargs={"pk": self.user_test2.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
