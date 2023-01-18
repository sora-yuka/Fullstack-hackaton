import uuid
from django.db import models
# from applications.product.models import Product
# from applications.account.models import CustomUser



# class Order(models.Model):
    
#     ORDER_STATUS = (
#         ('In proccess', 'In proccess'),
#         ('Canceled', 'Canceled'),
#         ('Delivering', 'Delivering'),
#         ('Completed', 'Completed'),
#     )
    
#     status = models.CharField(max_length=50, choices=ORDER_STATUS, null=True, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     amount = models.PositiveIntegerField()
#     address = models.CharField(max_length=50)
#     number = models.CharField(max_length=30)
#     is_confirm = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     activation_code = models.UUIDField(default=uuid.uuid4)
    
#     def save(self, *args, **kwargs):
#         self.total_price = self.amount * self.product.price
#         return super().save(*args, **kwargs)