import tempfile
from django.test import TestCase, override_settings, RequestFactory
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient
from .models import Participant
from .views import MatchParticipantView


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class CreateParticipantTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_participant(self):
        url = reverse('api_clients:create')
        
        with open('media/img/default_avi.png', 'rb') as file:
            file_content = file.read()
            
        avatar = SimpleUploadedFile("avatar.png", 
                                    file_content, 
                                    content_type="image/png")

        data = {
            'avatar': avatar,
            'gender': 'M',
            'first_name': 'Ivan',
            'last_name': 'Petrov',
            'email': 'abc@mail.ru',
            'password': '123456'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED, 
                         msg=response.data)
        self.assertEqual(Participant.objects.count(), 1)

        participant = Participant.objects.first()
        
        self.assertEqual(participant.gender, 'M')
        self.assertEqual(participant.first_name, 'Ivan')
        self.assertEqual(participant.last_name, 'Petrov')
        self.assertEqual(participant.email, 'abc@mail.ru')
        
        participant.avatar.delete()
        

class MatchParticipantViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.ivan = Participant.objects.create(
            username='Ivan',
            first_name='Ivan',
            email='abc@mail.ru',
            password='123456',
            gender='M',
        )
        self.masha = Participant.objects.create(
            username='Masha',
            first_name='Masha',
            email='123@mail.ru',
            password='123456',
            gender='F',
        )

    def test_match_participant(self):
        ivan_request = self.factory.post(
            f'/api/clients/{self.ivan.pk}/match/',
            {'target_id': self.masha.pk},
        )
        ivan_response = MatchParticipantView.as_view()(ivan_request, 
                                                   pk=self.ivan.pk)
        self.assertEqual(ivan_response.status_code, status.HTTP_200_OK)
        self.assertEqual(ivan_response.data['message'], 
                         'Оценка участника сохранена.')

        self.assertEqual(list(self.ivan.sympathy.all()), 
                         [self.masha])
        self.assertFalse(self.masha.sympathy.exists())

        masha_request = self.factory.post(
            f'/api/clients/{self.masha.pk}/match/',
            {'target_id': self.ivan.pk},
        )
        masha_response = MatchParticipantView.as_view()(masha_request, 
                                                   pk=self.masha.pk)
        self.assertEqual(masha_response.status_code, status.HTTP_200_OK)
        self.assertEqual(masha_response.data['message'], 
                         f'Вы понравились {self.ivan.first_name}!'
                         f' Почта участника: {self.ivan.email}')

        self.assertEqual(list(self.masha.sympathy.all()), 
                         [self.ivan])
        self.assertEqual(list(self.ivan.sympathy.all()), 
                         [self.masha])
