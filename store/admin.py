from django.contrib import admin
from . models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock', 'Category', 'modified_date', 'is_available')
    prepopulated_fields = {'Slug': ('Name', )}

admin.site.register(Product, ProductAdmin)