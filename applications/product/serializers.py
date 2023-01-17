from rest_framework import serializers
from applications.product import Image, Product


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    file_image = ImageSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Product
        fields = '__all__'