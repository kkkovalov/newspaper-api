from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserAccountManager(BaseUserManager):
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        email = str.lower(email)

        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **kwargs):
        pass

    def create_superuser(self, email, password=None, **kwargs):
        pass


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True, blank=False, verbose_name="Email"
    )
    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Full name"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email
