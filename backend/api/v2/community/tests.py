import io
import mock
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files import File

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from backend.community.models import Groups
from .serializers import GroupSerializer


class CommunityTests(APITestCase):

    def setUp(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'photo.jpg'

        user_test1 = User.objects.create_user(username='test', password="1q2w3e")
        user_test1.save()
        user_test2 = User.objects.create_user(username='test2', password="1q2w3e4r5t")
        user_test2.save()

        self.one_group = Groups.objects.create(
            title="Python",
            founder=user_test2,
            desc="Test group",
            miniature=file_mock.name,
            image=file_mock.name
        )

        image = io.BytesIO()
        Image.new('RGB', (150, 150)).save(image, 'JPEG')
        image.seek(0)
        min_file = SimpleUploadedFile('image.jpg', image.getvalue())

        Image.new('RGB', (1152, 2048)).save(image, 'JPEG')
        image.seek(0)
        image_file = SimpleUploadedFile('image2.jpg', image.getvalue())

        self.data = {
            "title": "MyGroup",
            "desc": "MyDesc",
            "group_variety": "private",
            "miniature": min_file,
            "image": image_file
        }

        self.user_test1_token = Token.objects.create(user=user_test1)
        self.user_test2_token = Token.objects.create(user=user_test2)

    def test_create_invalid_group(self):
        response = self.client.post(reverse('create_group'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_valid_group(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test2_token.key)
        response = self.client.post(reverse('create_group'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_enter_invalid_group(self):
        response = self.client.post(
            reverse('enter_group', kwargs={"pk": self.one_group.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_enter_valid_group(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.post(
            reverse('enter_group', kwargs={"pk": self.one_group.id}), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_groups_list(self):
        response = self.client.get(reverse('list_groups'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_fail_group_detail(self):
        response = self.client.get(reverse('detail_group', kwargs={'pk': 50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_group_detail(self):
        response = self.client.get(reverse('detail_group', kwargs={'pk': self.one_group.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Python")

    # def test_entry_group(self):
    #     response = self.client.get(reverse('detail_group', kwargs={'pk': self.one_group.id}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     serializer_data = GroupSerializer(self.one_group).data
        # response_data = json.dumps(response.content)
        # response_data = response.data

        # self.assertEqual(serializer_data, response.json().get("results"))