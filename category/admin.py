from django.contrib import admin
from . models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Name', )}
    list_display = ('Name', 'Slug')
admin.site.register(Category, CategoryAdmin)