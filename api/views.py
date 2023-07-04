from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParticipantSerializer
from django.core.files.base import ContentFile
from PIL import Image
import tempfile
import os
from django.conf import settings

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
                
                participant.avatar.save('avatar.png', ContentFile(avatar_image.tobytes()))
                
                os.remove(temp_image_path)
                os.rmdir(temp_dir)
            
            participant.save()
            return Response({'message': 'Участник успешно создан'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
