from django.contrib import admin
from applications.feedback.models import Favourite
from applications.product.models import Product, Image

class FileAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        FileAdmin
    ]
    list_display = ['name', 'id', 'price', 'author']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Favourite)