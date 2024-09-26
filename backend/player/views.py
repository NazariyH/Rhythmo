from django.shortcuts import render, get_object_or_404, get_list_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import SongSerializer, PlaylistSerializer
from .models import Song, Playlist


# Create your views here.

class SongView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        songs = get_list_or_404(Song, author=request.user.id)
        serializer = SongSerializer(songs, many=True)

        return Response({"songs": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReactSong(APIView):
    def get(self, request, id, *args, **kwargs):
        song = get_object_or_404(Song, id=id)
        is_liked = song.likes.filter(id=request.user.id).exists()

        return Response({'song_is_liked': is_liked})
    
    def patch(self, request, id, *args, **kwargs):
        song = get_object_or_404(Song, id=id)

        if song.likes.filter(id=request.user.id).exists():
            song.likes.remove(request.user)
            return Response({'song_is_liked': False, 'song_likes_length': song.likes.count()}, status=status.HTTP_200_OK)
        song.likes.add(request.user)
        return Response({'song_is_liked': True, 'song_likes_length': song.likes.count()}, status=status.HTTP_200_OK)

    

class DeleteSong(APIView):
    def delete(self, request, id, *args, **kwargs):
        song = get_object_or_404(Song, id=id)
        
        if song.author == request.user:
            song.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message": "You're not allowed to remove songs that are not yours"})
        

class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        playlists = get_list_or_404(Playlist, author=request.user.id)
        
        serializer = PlaylistSerializer(playlists, many=True)

        return Response({"playlists": serializer.data}, status=status.HTTP_200_OK)
        