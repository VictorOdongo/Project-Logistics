from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.get_full_name()