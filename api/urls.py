from django.urls import path
from .views import ParticipantListView

urlpatterns = [
    path('list/', ParticipantListView.as_view(), name='list'),
]