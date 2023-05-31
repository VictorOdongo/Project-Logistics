from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=10, unique=True, blank=False, default='xx234xx')
    firstname = models.CharField(max_length=10, blank=True)
    lastname = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=255, blank=False)
   
class Entreprise(models.Model):
    businessname = models.CharField(null=False, max_length=20, unique=True)
    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=255, blank=False)
    
class Driver(models.Model):

    firstname = models.CharField(max_length=10, blank=False)
    lastname = models.CharField(max_length=10, blank=False)
    licence = models.CharField(max_length=10, blank=False, primary_key=True, unique=True)
    mobile = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
                
    def __str__(self):
        return self.user.username
    
#class Personal(AbstractUser):
    
    # pass
