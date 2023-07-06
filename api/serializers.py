from rest_framework import serializers
from .models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Participant
        fields = '__all__'
