from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Personal(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    mobile = models.IntegerField()
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    
# class CustomUser(AbstractUser):
    
    # pass
