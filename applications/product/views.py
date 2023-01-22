from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from applications.feedback.views import FeedbackMixin
from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from applications.product.permissions import IsProductOwnerOrReadOnly, IsFeedbackOwner
from rest_framework.viewsets import ModelViewSet
import logging

logger = logging.getLogger(__name__)

class ProductViewSet(ModelViewSet, FeedbackMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name']
    order_fields = ['price']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_permissions(self):
        print(self.action)
        if self.action == 'delete_comment':
            return [IsFeedbackOwner()]
        return super().get_permissions()
    