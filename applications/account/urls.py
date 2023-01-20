from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.account.views import (
    RegisterAPIView, ActivationAPIView,
    ChangePasswordAPIView, ForgotPasswordAPIView,
    ForgotPasswordConfirmAPIView,
    ProfileAPIView
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("confirm/<uuid:activation_code>/", ActivationAPIView.as_view()),
    path("change_password/", ChangePasswordAPIView.as_view()),
    path("forgot_password/", ForgotPasswordAPIView.as_view()),
    path("forgot_password_complete/", ForgotPasswordConfirmAPIView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
]
