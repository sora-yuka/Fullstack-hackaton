from rest_framework.routers import DefaultRouter
from django.urls import include, path
from applications.feedback.views import CommentViewSet

router = DefaultRouter()
# router.register('comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls))    
]