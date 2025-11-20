from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('agent', 'Travel Agent'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=USER_ROLES, default='customer')
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username

# Create your models here.
