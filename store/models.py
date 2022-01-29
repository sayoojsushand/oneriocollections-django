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


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value
