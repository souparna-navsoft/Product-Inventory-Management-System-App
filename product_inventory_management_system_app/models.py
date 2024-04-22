from django.db import models
import uuid


class Brand(models.Model):
    name = models.CharField(max_length=255 , unique=True , blank=False)
    country = models.CharField(max_length=100 , blank=False)
    founded_year = models.PositiveIntegerField(default=0 , blank=False)
    description = models.TextField(default="default brand" , blank=True , null=True)

class Color(models.Model):
    name = models.CharField(max_length=255 , unique=True , blank=False)
    description = models.TextField(default="default color" , blank=True , null=True)

class Product(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    sku = models.CharField(max_length=50 , unique=True , blank=False)
    name = models.CharField(max_length=255 , blank=False)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    color = models.ForeignKey(Color , on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=50 , decimal_places=2 , blank=False)
    description = models.TextField(default="default description" , blank=True , null=True)
    reviews = models.TextField(default="default reviews" , blank=True , null=True)

class Store(models.Model):
    name = models.CharField(max_length=255 , unique=True , blank=False)
    address = models.CharField(max_length=255 , blank=False)
    phone_number = models.CharField(max_length=50 , unique=True , blank=False)
    email = models.EmailField(max_length=100 , unique=True , blank=False)
    rating = models.DecimalField(max_digits=50 , decimal_places=2 , blank=False)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False)
    last_stocked_date = models.DateField(blank=False)
    is_available = models.BooleanField(default=True , blank=False)


