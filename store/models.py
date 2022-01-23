from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Slug = models.SlugField(max_length=200, unique=True)
    Description = models.TextField(max_length=500, blank=True)
    Price = models.IntegerField()
    Image = models.ImageField(upload_to='photos/products')
    Stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.Category.Slug, self.Slug])

    def __str__(self):
        return self.Name
