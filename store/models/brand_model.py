from django.db import models
from django.conf import settings


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Brand name')
    # category = 
    description = models.TimeField(max_length=1020, verbose_name='Description')
    