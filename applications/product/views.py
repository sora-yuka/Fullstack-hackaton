import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from applications.feedback.models import Rating
from applications.feedback.serializers import RatingSerializer
from applications.feedback.views import FeedbackMixin
from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from applications.product.permissions import IsProductOwnerOrReadOnly, IsFeedbackOwner
# from rest_framework.viewsets import ModelViewSet
from core.product.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import logging

logger = logging.getLogger("main")

class PaginationApiView(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'book_pages'


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
        if self.action == 'delete_comment':
            return [IsFeedbackOwner()]
        return super().get_permissions()
    
    
    @action(detail=False, methods=['GET'])
    def popular(self, request, *args, **kwargs):
        products = Product.objects.filter(ratings__rating__gt=7.0).distinct()
        print(products)
        serializer = ProductSerializer(products, many=True)
        logger.info("User listing popular.")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def recommend(self, request, pk=None):
        category = self.get_object().category
        queryset = Product.objects.filter(category=category)
        serializers = ProductSerializer(queryset, many=True)
        logger.info("User listing recomended product.")
        return Response(serializers.data)