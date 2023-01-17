from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from applications.account.serializers import (RegisterSerializer
    # RegisterSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, 
    # ForgotPasswordCompleteSerializer
)

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('You have successfully registred. '
                        'We sent an activation email',
                        status=status.HTTP_201_CREATED
                        )