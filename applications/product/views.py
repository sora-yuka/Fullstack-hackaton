from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from applications.product.models import Product
from rest_framework.viewsets import mixins, GenericViewSet
from applications.product.serializers import ProductSerializer
from applications.product.permissions import IsProductOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


class LargeResultSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_parm = 'page_size'
    max_page_size = 10000


class ProductViewSet(mixins.ListModelMixin, GenericViewSet):
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

    @action(detail=True, methods=['GET'])
    def recommend(self, request, pk=None):
        category = self.get_object().category
        queryset = Product.objects.filter(category=category)
        serializers = ProductSerializer(queryset, many=True)
        return Response(serializers.data)