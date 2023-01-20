from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from applications.feedback.views import FeedbackMixin
from applications.product import views

router = DefaultRouter()
router.register('', views.ProductViewSet)


urlpatterns = [
    path('<int:pk>/comment/', views.ProductViewSet.as_view({'post': 'add_comment'})),
    path('comment/<int:pk>/', views.ProductViewSet.as_view({'delete': 'delete_comment'})),
    path('', include(router.urls)),  
]
