from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

# Create your models here.



class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff:bool, is_superuser:bool, first_name:str=None, last_name:str=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            first_name=first_name,
            last_name=last_name,
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

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()