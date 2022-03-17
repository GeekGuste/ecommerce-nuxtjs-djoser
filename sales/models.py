import datetime
from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=200)
    is_active = models.BooleanField()
    #on met category entre côtes et ça référence toujours la catégorie
    parent = models.ForeignKey("Category", on_delete=models.CASCADE)

class VariantType(models.Model):
    label = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    variant_type = models.ForeignKey(VariantType, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    description = models.TextField()
    qte_stock = models.IntegerField(default=100)
    principal_image = models.ImageField(upload_to='products')
    is_variant = models.BooleanField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    promo_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.BooleanField()
    pub_date = models.DateTimeField(auto_now=True)

class Image(models.Model):
    photo = models.ImageField(upload_to = 'products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Video(models.Model):
    file = models.FileField(upload_to='products_video')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Tags(models.Model):
    label = models.CharField(max_length=100)


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
