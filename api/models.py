from django.db import models
from django.contrib.auth.models import AbstractUser


class Participant(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    )
    
    avatar = models.ImageField(upload_to='media/avatars/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
