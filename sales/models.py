import datetime
from django.db import models
from numpy import product
from users.models import User

# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=200)
    is_active = models.BooleanField()
    #on met category entre côtes et ça référence toujours la catégorie
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name="enfants")

class VariantType(models.Model):
    label = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parent = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, related_name="variants")
    variant_type = models.ForeignKey(VariantType, on_delete=models.CASCADE, null=True)
    label = models.CharField(max_length=200)
    description = models.TextField()
    qte_stock = models.IntegerField(default=100)
    principal_image = models.ImageField(upload_to='products', null=True)
    is_variant = models.BooleanField(default=False)
    variant_value = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=50)
    promo_price = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now=True)

class Image(models.Model):
    photo = models.ImageField(upload_to = 'products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

class Video(models.Model):
    file = models.FileField(upload_to='products_video')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="videos")

class Tags(models.Model):
    label = models.CharField(max_length=100)

class DeliveryZoneInfo(models.Model):
    zone = models.CharField(max_length=100)
    delivery_charges = models.DecimalField(max_digits=15, decimal_places=2)

class DeliveryAddress(models.Model):
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    additional_informations = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
