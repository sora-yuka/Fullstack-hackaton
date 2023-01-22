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
            print('*************************')
            print('******************AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA************')
            return [IsFeedbackOwner()]
        return super().get_permissions()
    
    
    # def add_comment(self, request, pk=None):
    #     try:
    #         product = self.get_object()
    #         comment = request.data['comment']
    #         user = request.user
    #         comment_obj = Comment.objects.create(owner=user, product=product, comment=comment)
    #         comment_obj.save()
    #         return Response({'msg': 'comment added'}, status=status.HTTP_201_CREATED)
    #     except MultiValueDictKeyError:
    #         return Response({'msg': 'field comment is required'}, status=status.HTTP_400_BAD_REQUEST)
        
    # def delete_comment(self, request, pk):
    #     comment = get_object_or_404(Comment, pk=pk)
    #     comment.delete()
    #     return Response({'msg': 'comment deleted'}, status=status.HTTP_204_NO_CONTENT)    
    
    