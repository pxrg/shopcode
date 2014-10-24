from shop.models import Product
from django.db import models


class Book(Product):
    author = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to='img/products/book')
    isbn = models.CharField(max_length=255)

    class Meta:
        ordering = ['author']
