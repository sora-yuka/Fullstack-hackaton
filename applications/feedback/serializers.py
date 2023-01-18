from rest_framework import serializers
from applications.feedback.models import Favorite


class FavoriteSerializer(serializers):
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model = Favorite
        fields = "__all__"