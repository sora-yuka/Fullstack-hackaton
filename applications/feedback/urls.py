from rest_framework.routers import DefaultRouter
from django.urls import include, path
from applications.feedback.views import CommentViewSet

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls))    
]
