import django_filters
from .models import Participant
from geopy.distance import great_circle


class ParticipantFilter(django_filters.FilterSet):
    gender = django_filters.ChoiceFilter(choices=Participant.GENDER_CHOICES)
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    max_distance = django_filters.NumberFilter(method='filter_max_distance')

    def filter_max_distance(self, queryset, name, value):
        queryset = queryset.exclude(pk=self.request.user.id)
        user_longitude = self.request.user.longitude
        user_latitude = self.request.user.latitude
        if user_longitude is not None and user_latitude is not None:
            queryset = queryset.filter(
                longitude__isnull=False,
                latitude__isnull=False
            )
            user_location = (user_latitude, user_longitude)
            for participant in queryset:
                participant_location = (participant.latitude, participant.longitude)
                distance = great_circle(user_location, participant_location).kilometers
                if float(distance) >= float(value):
                    queryset = queryset.exclude(pk=participant.pk)
            return queryset
        return queryset

    class Meta:
        model = Participant
        fields = ['gender', 'first_name', 'last_name', 'max_distance']
