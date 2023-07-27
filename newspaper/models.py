from django.db import models
from django.contrib.auth.models import User
from time import timezone
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
    
class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Topic name")
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=500, verbose_name="Article name", blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False, blank=False)
    body = models.TextField(verbose_name="Article body")
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # images = 
    
    def __str__(self):
        return self.name
    
    def get_short_body(self):
        return self.body[:100] + '...'

    
