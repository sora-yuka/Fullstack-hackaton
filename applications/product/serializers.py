from rest_framework import serializers
from applications.feedback.models import Comment
from applications.feedback.serializers import CommentSerializer
from applications.product.models import Product
from django.db.models import Avg


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ["owner"]
        
       
    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        return product
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        comment = Comment.objects.filter(product=instance.id)
        serializer = CommentSerializer(comment, many=True)
        comments = serializer.data
        
        rep['price'] = float(instance.price) - float(instance.discount/100)*float(instance.price)
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        rep['comment'] = comments
        return rep
    