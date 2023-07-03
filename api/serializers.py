from rest_framework import serializers
from .models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Participant
        fields = ['id', 'avatar', 'gender', 'first_name', 'last_name', 'email', 'password']
