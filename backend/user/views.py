from django.shortcuts import render, get_object_or_404, get_list_or_404
from player.models import Song

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from player.serializers import SongSerializer


# Create your views here.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class ProfileView(APIView):
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, user=pk)
        songs_list = get_list_or_404(Song, author=pk)            


        serializer_profile = ProfileSerializer(profile)
        serializer_song = SongSerializer(songs_list, many=True)

        is_current_user = False

        if request.user == profile.user:
            is_current_user = True

        
        return Response({"profile": serializer_profile.data, "is_current_user": is_current_user, "songs": serializer_song.data}, status=status.HTTP_200_OK)
            

class OwnProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user.id)
        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data, "is_current_user": True}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        profile, created = Profile.objects.get_or_create(user=request.user)

        request_data = request.data.copy()
        request_data['user'] = request.user.id

        if request_data['profileImage'] == '':
            request_data['profileImage'] = profile.profileImage

        serializer = ProfileSerializer(instance=profile, data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
