from django.contrib import admin
from applications.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'price', 'author']
    

admin.site.register(Product, ProductAdmin)
