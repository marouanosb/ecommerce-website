from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    address = models.TextField()
    contact = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    description = models.TextField()

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
