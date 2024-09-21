from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


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
        serializer = ProfileSerializer(profile)
        
        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
            

class OwnProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user.id)
        serializer = ProfileSerializer(profile)

        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)