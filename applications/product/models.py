from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()

CATEGORY_NAME = (
    ('Drama', 'Drama'),
    ('Fantasy', 'Fantasy'),
    ('Romance', 'Romance'),
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_NAME)
    amount = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')