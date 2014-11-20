from shop.models import Product
from django.db import models
from django.forms import forms


class Book(Product):
    author = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to='img/products/book')
    isbn = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['author']
