from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from applications.feedback.views import FeedbackMixin
from applications.product.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet)


urlpatterns = [
    # path('<int:pk>/rating/',    .as_view(), ),
    path('<int:pk>/like/', ProductViewSet.as_view({'post': 'like'})),
    path('<int:pk>/comment/', ProductViewSet.as_view({'post': 'add_comment'})),
    path('comment/<int:pk>/', ProductViewSet.as_view({'delete': 'delete_comment'})),
    path('', include(router.urls)),  
]
