from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Product name',)
    price = models.FloatField(blank=False, verbose_name='Price')
    description = models.TimeField(max_length=1020, verbose_name='Description')
    # rating = models.One
    # picture_url = 
    # brand = models.
    # type = 
    
    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Brand name')
    # category = 
    description = models.TimeField(max_length=1020, verbose_name='Description')
    

class Type(models.Model):
    pass

class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product name')
    

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    rating_value = models.FloatField(blank=False, verbose_name='Rating value')
    text = models.TextField(blank=True, verbose_name='Rating text')