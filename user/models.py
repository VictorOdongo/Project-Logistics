from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=15, unique=True, blank=False, default='xx234xx')
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.user.username
    
   
class Entreprise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    business_name = models.CharField(null=False, max_length=20, unique=True)
    firstname = models.CharField(max_length=20, blank=False)
    lastname = models.CharField(max_length=20, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.user.username
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=False)
    lastname = models.CharField(max_length=20, blank=False)
    license = models.CharField(max_length=15, blank=False, primary_key=True, unique=True)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
                
    def __str__(self):
        return self.user.username
    
#class Personal(AbstractUser):
    
    # pass
