from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer/avatars/', blank=True, null=True)
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=False)
    mobile = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.user.username
    
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
                
    def __str__(self):
        return self.user.username
    
#class Personal(AbstractUser):
    
    # pass
