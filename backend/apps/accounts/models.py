

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractUser

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None,role='customer', **extra_fields):
        if not username:
            raise ValueError("The Username field is required.")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role,**extra_fields)
        user.set_password(password)  # ✅ hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)


# Custom User Model
class Users(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('owner', 'Restaurant Owner'),
        ('driver', 'Delivery Driver'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    owner_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
