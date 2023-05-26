from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Personal(models.Model):
    username = models.CharField(max_length=10, primary_key=True, unique=True)
    lastname = models.CharField(max_length=10, blank=False)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    password = models.CharField(blank=False)
    
class Entreprise(models.Model):
    businessname = models.CharField(max_length=20, primary_key=True unique=True)
    businesssize = models.IntegerField(blank=False)
    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    password = models.CharField(blank=False)
    
class Driver(models.Model):
    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    licence = models.CharField(max_length=10, blank=False, primary_key=True, unique=True)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    password = models.CharField(blank=False)
                
    def _str_(self):
        return self.user.username
    
# class CustomUser(AbstractUser):
    
    # pass
