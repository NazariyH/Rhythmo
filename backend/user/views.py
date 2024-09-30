from django.shortcuts import render, get_object_or_404, get_list_or_404
from player.models import Song, Playlist
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from player.serializers import SongSerializer, PlaylistSerializer


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
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, user=pk)
        serializer_profile = ProfileSerializer(profile)

        try: 
            songs_list = get_list_or_404(Song, author=pk)
            serializer_song = SongSerializer(songs_list, many=True)
            songs = serializer_song.data
        except Http404:
            songs = None

        try:
            playlists_list = get_list_or_404(Playlist, author=pk)         
            serializer_playlist = PlaylistSerializer(playlists_list, many=True)
            playlists = serializer_playlist.data
        except Http404:
            playlists = None

        is_current_user = False

        if request.user == profile.user:
            is_current_user = True

        is_subscribed = profile.followers.filter(id=request.user.id).exists()

        response = {
            "profile": serializer_profile.data, 
            "user_id": profile.user.id,
            "songs": songs, 
            "playlists": playlists,
            "is_current_user": is_current_user, 
            "is_subscribed": is_subscribed
        }
        
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, user=pk)
        
        if profile.followers.filter(id=request.user.id).exists():
            profile.followers.remove(request.user)
            return Response({'subscribed': False, 'subscribers_count': profile.followers.count()}, status=status.HTTP_200_OK)
        else:
            profile.followers.add(request.user)
            return Response({'subscribed': True, 'subscribers_count': profile.followers.count()})


class OwnProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user.id)
        serializer = ProfileSerializer(profile)

        return Response({'profile': serializer.data, 'is_current_user': True}, status=status.HTTP_200_OK)
    
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
