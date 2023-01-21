from rest_framework import serializers
from applications.feedback.models import Comment, Like, Rating
from django.contrib.auth import get_user_model

User = get_user_model()


# class FavoriteSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source="owner.username")
    
#     class Meta:
#         model = Favorite
#         fields = "__all__"
        







class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.usarname')
    rating = serializers.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = Rating
        fields = ['rating']
        

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.usarname')
    
    class Meta:
        model = Like
        fields = '__all__'
        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()






























# class RatingSerializer(serializers.ModelSerializer):
#     rating = serializers.IntegerField(min_value=1, max_value=5)

#     class Meta:
#         model = Rating
#         fields = ['rating']


# class FanSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()

#     class Meta:
#         model = User
#         fields = (
#             'email',
#         )

#     @staticmethod
#     def get_email(obj):
#         return obj.get_email()