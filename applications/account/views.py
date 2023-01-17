from django.shortcuts import render
from rest_framework.generics import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from applications.account.serializers import (
    RegisterSerializer
)

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request, *args,) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            "You have successfully registered. We send an activation code.",
            status=status.HTTP_201_CREATED,
        )