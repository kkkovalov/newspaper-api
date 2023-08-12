from django.db import models
from django.conf import settings

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