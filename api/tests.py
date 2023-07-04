import os
from django.test import TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient
from .models import Participant
import tempfile
from PIL import Image


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class CreateParticipantTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_participant(self):
        url = reverse('api_clients:create')
        
        with open('media/img/default_avi.png', 'rb') as file:
            file_content = file.read()
            
        avatar = SimpleUploadedFile("avatar.png", file_content, content_type="image/png")

        data = {
            'avatar': avatar,
            'gender': 'M',
            'first_name': 'Ivan',
            'last_name': 'Petrov',
            'email': 'abc@mail.ru',
            'password': '123456'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(Participant.objects.count(), 1)

        participant = Participant.objects.first()
        
        self.assertEqual(participant.gender, 'M')
        self.assertEqual(participant.first_name, 'Ivan')
        self.assertEqual(participant.last_name, 'Petrov')
        self.assertEqual(participant.email, 'abc@mail.ru')
        
        participant.avatar.delete()
        
