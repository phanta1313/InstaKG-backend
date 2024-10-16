from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, db_index=True, unique=True)

    USERNAME_FIELD = 'username'

    @classmethod
    def create_user(ctx, username, password, **extra_fields):
        if not username:
            raise ValueError("The given email must be set")
        user = ctx(username=username, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user
