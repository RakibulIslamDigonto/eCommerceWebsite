from venv import create
from django.db import models
from coreApp.models import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    old_price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/products/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]

