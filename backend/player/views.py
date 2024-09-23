from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song


# Create your views here.

class SongView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        songs = Song.objects.filter(author=request.user.id)
        serializer = SongSerializer(songs, many=True)

        return Response({"songs": serializer.data}, status=status.HTTP_200_OK)