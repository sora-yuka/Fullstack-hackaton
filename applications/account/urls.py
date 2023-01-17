from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from applications.account.views import (
    RegisterAPIView, ActivationAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("confirm/<uuid:activation_code>/", ActivationAPIView.as_view()),
]
