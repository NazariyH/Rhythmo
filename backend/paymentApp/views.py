from django.shortcuts import render, get_object_or_404
from user.models import Profile

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PaymentProcess(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user.id)        
        return Response({'is_premium': profile.is_premium}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user.id)
        profile.is_premium = True
        profile.save()

        return Response(status=status.HTTP_200_OK)