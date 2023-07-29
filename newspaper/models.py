from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
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

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

    
class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    username = None
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()