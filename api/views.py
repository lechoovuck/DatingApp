from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParticipantSerializer

class CreateParticipantView(APIView):
    def post(self, request):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            participant = serializer.save()
            participant.set_password(request.data['password'])
            participant.save()
            return Response({'message': 'Участник успешно создан'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
