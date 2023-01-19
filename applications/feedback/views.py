from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from applications.feedback.serializers import CommentSerializer, FavoriteSerializer
from applications.feedback.permissions import IsCommentOwner, IsFavoriteOwner
from applications.feedback.models import Comment, Favorite


class FavoriteViewSet(ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    permissions_classes = [IsFavoriteOwner]
    
    def perform_create(self, serializer):
        serializer.save(self.request.user)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user.id)
        return queryset
    
    
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permissions_classes = [IsCommentOwner]
    
    def perform_create(self, serializer):
        serializer.save(self.request.user)
