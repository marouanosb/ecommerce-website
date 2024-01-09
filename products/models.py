from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    class Categories(models.TextChoices):
        FOOD = 'FOOD', 'Nourriture'
        COSMETIC = 'COSMETIC', 'Cosmetique'
        ELECTRONIC = 'ELECTRONIC', 'Electronique'
        CLOTHS = 'CLOTHS', 'Vetements'
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10,choices=Categories)
    image = models.ImageField()
    name = models.CharField(max_length=20)
    reviews = models.IntegerField()
    reviews_number = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    vendor = models.OneToOneField(User ,on_delete=models.CASCADE)