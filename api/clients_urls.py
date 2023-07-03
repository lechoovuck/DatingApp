from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateParticipantView.as_view(), name='create'),
]
