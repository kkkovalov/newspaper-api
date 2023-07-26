from django.db import models
from django.contrib.auth.models import User
from time import timezone
from django.contrib import admin
# Create your models here.

class Reader(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="Reader")
    # picture = 
    # preferrences = 
    
    def __str__(self):
        return self.user.username

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Creator")
    department = models.CharField(max_length=200, verbose_name="Department name", default="Newspaper")
    
    def __str__(self):
        return self.user.username
    
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
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=False,blank=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False, blank=False)
    body = models.TextField(verbose_name="Article body")
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # images = 
    
    def __str__(self):
        return self.name
    
    
