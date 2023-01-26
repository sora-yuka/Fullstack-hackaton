from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_NAME = (
    ('Thrieler', 'Thrieler'),
    ('Mystery', 'Mystery'),
    ('Drama', 'Drama'),
    ('Fantasy', 'Fantasy'),
    ('Romance', 'Romance'),
    ('Anti utopia', 'Anti utopia'),
    ('Utopia', 'Utopia'),
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_NAME)
    amount = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.ImageField(upload_to='image/')
   
    def __str__(self) -> str:
        return self.name