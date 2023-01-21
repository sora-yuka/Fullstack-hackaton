# from rest_framework.viewsets import ModelViewSet
from applications.feedback.models import Comment, Favourite, Like, Rating
# from rest_framework.views import APIView
from applications.feedback.permissions import IsCommentOwner
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from applications.feedback.serializers import CommentSerializer, RatingSerializer
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


class FeedbackMixin:
    def add_comment(self, request, pk=None):
        try:
            product = self.get_object()
            comment = request.data['comment']
            user = request.user
            comment_obj = Comment.objects.create(owner=user, product=product, comment=comment)
            comment_obj.save()
            return Response({'msg': 'comment added'}, status=status.HTTP_201_CREATED)
        except MultiValueDictKeyError:
            return Response({'msg': 'field comment is required'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete_comment(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({'msg': 'comment deleted'}, status=status.HTTP_204_NO_CONTENT) 
    
    
    def like(self, request, pk=None, *args, **kwargs):
        try:
            like_obj, _ = Like.objects.get_or_create(owner=request.user, product_id=pk)
            like_obj.like = not like_obj.like
            like_obj.save()
            msg = 'liked'
            if not like_obj.like:
                msg = 'unliked'
            return Response(f'You {msg} it')
        except:
            return Response('Something went wrong')
        
        
    def rating(self, request, pk=None, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            rating_obj, _ = Rating.objects.get_or_create(owner=request.user, product_id=pk)
            rating_obj.rating = request.data['rating']
            rating_obj.save()
            msg = request.data['rating']
            return Response(f'You give {msg} points to this book')
        except:
            return Response('Something went wrong')
        
    
    def favourite(self, request, pk=None, *args, **kwargs):
        try:
            fav = []
            fav_obj, _ = Favourite.objects.get_or_create(owner=request.user, product_id=pk)
            fav_obj.favourite = not fav_obj.favourite
            fav.append(fav_obj)
            fav_obj.save()
            msg = 'Added to favourites'
            if not fav_obj.favourite:
                print(fav_obj)
                print(fav)
                fav.remove(fav_obj)
                fav_obj.delete()
                msg = 'Deleted from favourites'
            return Response(msg)
        except:
            return Response('Something went wrong')
       
