import django_filters
from .models import Participant

class ParticipantFilter(django_filters.FilterSet):
    gender = django_filters.ChoiceFilter(choices=Participant.GENDER_CHOICES)
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Participant
        fields = ['gender', 'first_name', 'last_name']