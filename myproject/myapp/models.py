from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import models

class User(AbstractUser):
    # Add any additional fields here
    name = models.CharField(max_length=255,unique=False)
    age = models.IntegerField(default=0)

    # Specify unique related names for groups and user permissions
    groups = models.ManyToManyField(Group, related_name='myapp_users')
    user_permissions = models.ManyToManyField(Permission, related_name='myapp_users')

    # Remove the password field
    password = None
    username = None 

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['age']

