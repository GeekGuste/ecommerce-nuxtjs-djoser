from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField('email address', unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']