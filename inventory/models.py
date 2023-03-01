from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    maincontact = models.CharField(max_length=255, null=True)
    telephone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    country = models.TextField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return self.name