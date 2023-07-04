from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateParticipantView.as_view(), name='create'),
    path('<int:pk>/match/', MatchParticipantView.as_view(), name='match'),

]
