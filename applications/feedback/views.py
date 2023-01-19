from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from applications.feedback.serializers import FavoriteSerializer
from applications.feedback.permissions import IsFavoriteOwner
from applications.feedback.models import Favorite


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
