from django.db import models
from django.contrib import admin
from django.conf import settings
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
@receiver(pre_save)
def _pre_save_slugify(sender, instance, **kwargs):
    list_of_models = {'Tag', 'Topic', 'Article'}
    if sender.__name__ in list_of_models:
            instance.slug_name = slugify(instance.name)

    
class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Topic name", blank=False, unique=True)
    description = models.CharField(max_length=255, verbose_name="Description", blank=True)
    slug_name = models.CharField(max_length=100, verbose_name="Slug name", blank=False, unique=True, default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
    
# Model class for Tag, returns 'name' field by default.
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name="Name")
    slug_name = models.CharField(max_length=100, blank=False, unique=True,verbose_name="Slug name", default='')
    
    def __str__(self):
        return self.name

    # Meta related class for ordering
    class Meta:
        ordering = ['name']



class Article(models.Model):
    name = models.CharField(max_length=500, verbose_name="Article name", blank=False, unique=True)
    slug_name = models.CharField(max_length=500, verbose_name="Slug name", blank=False, unique=True, default='')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False,blank=False)
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