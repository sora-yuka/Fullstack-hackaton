from django.db import models
from applications.account.models import CustomUser
from applications.product.models import Product


class Favorite(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorites")
    
    def __str__(self):
        return self.product.title()