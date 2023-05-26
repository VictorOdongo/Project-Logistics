from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Personal(models.Model):
    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    id = models.AutoField(primary_key=True, blank=False,unique=True)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    password = models.CharField(blank=False)
    
class Entreprise(models.Model):
    businessname = models.CharField(max_length=20, blank=False, unique=True)
    businesssize = models.IntegerField(blank=False)
    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    id = models.AutoField(primary_key=True, blank=False,unique=True)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    password = models.CharField(blank=False)
    
class Driver(models.Model):
    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    id = models.CharField(blank=False,unique=True)
    licence = models.CharField(max_length=10, blank=False, primary_key=True, unique=True)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=20, blank=False, unique=True)
    password = models.CharField(blank=False)
                
    
    
# class CustomUser(AbstractUser):
    
    # pass
