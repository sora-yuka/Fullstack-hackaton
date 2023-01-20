# from rest_framework.viewsets import ModelViewSet
from applications.feedback.models import Comment
# from rest_framework.views import APIView
from applications.feedback.permissions import IsCommentOwner
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import action
# from django.utils.datastructures import MultiValueDictKeyError

from applications.feedback.serializers import CommentSerializer
# from applications.product.models import Product
from rest_framework.generics import CreateAPIView, DestroyAPIView


#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#     permission_classes = [IsCommentOwner]
    
#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)
        

# class FeedbackMixin:
    # @action(methods=['POST'], detail=True)
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
        
        
    # @action(methods=['DELETE'], detail=True)
    # def delete_comment(self, request, pk, com_id):
    # # try:
    #     product = self.get_object()
    #     comment = request.data['comment']
    #     user = request.user
    #     comment_obj = Comment.objects.get(owner=user, product=product, pk=id)
    #     comment_obj.comment = comment
    #     comment_obj.delete()
    #     return Response({'msg': 'comment deleted'}, status=status.HTTP_204_NO_CONTENT)    
    # # except:
            
# class FeedbackMixin:        
#     class CommentCreateApiView(CreateAPIView):
#         queryset = Comment.objects.all()
#         serializer_class = CommentSerializer
#         permission_classes = [IsCommentOwner]
        
#         def post(self, request, *args, **kwargs):
#             instance = self.get_object()
#             serializer = self.get_serializer(instance)
#             return Response(serializer.data)
    
#     class CommentDestroyApiView(DestroyAPIView):
#         queryset = Comment.objects.all()
#         serializer_class = CommentSerializer
#         permission_classes = [IsCommentOwner]