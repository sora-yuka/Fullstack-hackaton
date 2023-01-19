from django.db import models
from applications.account.models import CustomUser
from applications.product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Favorite(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorites")
    
    def __str__(self):
        return self.product.title()
    
    
class Rating(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.owner} - {self.rating}'


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.product.title}'