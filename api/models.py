from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Participant(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    )
    
    avatar = models.ImageField(upload_to='media/avatars/', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sympathy = models.ManyToManyField('self', blank=True, symmetrical=False)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='participant_set', 
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='participant_set',
        related_query_name='user',
    )