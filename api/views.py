from PIL import Image
import tempfile
import os

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from .serializers import *
from .models import *
from .filters import *


class CreateParticipantView(APIView):
    def post(self, request):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            participant = serializer.save()
            participant.set_password(request.data['password'])

            avatar = request.FILES.get('avatar')
            if avatar:
                watermark_image_path = os.path.join(settings.BASE_DIR, 'media\\img\\watermark.png')
                temp_dir = tempfile.mkdtemp() 
                temp_image_path = os.path.join(temp_dir, 'avatar.png')
                
                with open(temp_image_path, 'wb') as temp_image_file:
                    for chunk in avatar.chunks():
                        temp_image_file.write(chunk)
                
                avatar_image = Image.open(temp_image_path)
                watermark_image = Image.open(watermark_image_path)
                
                avatar_width, avatar_height = avatar_image.size
                watermark_width, watermark_height = watermark_image.size
                
                x = (avatar_width - watermark_width) // 2
                y = (avatar_height - watermark_height) // 2
                
                avatar_image.paste(watermark_image, (x, y), watermark_image)
                # avatar_image.show()
                
                participant.avatar.save('avatar.png', 
                                        ContentFile(avatar_image.tobytes()))
                
                os.remove(temp_image_path)
                os.rmdir(temp_dir)
            
            participant.save()
            return Response({'message': 'Участник успешно создан'}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)


class MatchParticipantView(APIView):
    def post(self, request, pk):
        current_participant = get_object_or_404(Participant, pk=pk)
        target_participant = get_object_or_404(Participant, pk=request.data.get('target_id'))
        
        current_participant.sympathy.add(target_participant)
        if (target_participant.sympathy.filter(id=current_participant.id).exists() 
            and current_participant.sympathy.filter(id=target_participant.id).exists()):
            email_subject = f'Есть взаимная симпатия!'
            email_body = f'Вы понравились {target_participant.first_name}! Почта участника: {target_participant.email}'
            
            # send_mail(email_subject, 
            #           email_body, 
            #           settings.EMAIL_HOST_USER, 
            #           [current_participant.email, target_participant.email], 
            #           fail_silently=False)
            # TODO: SMTP
                        
            return Response({'message': email_body}, 
                            status=status.HTTP_200_OK)
        
        return Response({'message': 'Оценка участника сохранена.'}, 
                        status=status.HTTP_200_OK)


class ParticipantListView(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParticipantFilter
