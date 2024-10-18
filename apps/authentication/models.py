from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()



