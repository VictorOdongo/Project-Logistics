import uuid
from django.db import models
from django.utils import timezone
from user.models import Personal



class Category(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    SMALL_SIZE = "small"
    MEDIUM_SIZE = "medium"
    LARGE_SIZE = "large"
    SIZES = (
        (SMALL_SIZE, 'Small'),
        (MEDIUM_SIZE, 'Medium'),
        (LARGE_SIZE, 'Large')
    )

    CREATING_STATUS = 'creating'
    PROCESSING_STATUS = 'processing'
    PICKING_STATUS = 'picking'
    DELIVERING_STATUS = 'delivering'
    COMPLETED_STATUS = 'completed'
    CANCELLED_STATUS = 'cancelled'
    STATUSES = (
        (CREATING_STATUS, 'Creating'),
        (PROCESSING_STATUS, 'Processing'),
        (PICKING_STATUS, 'Picking'),
        (DELIVERING_STATUS, 'Delivering'),
        (COMPLETED_STATUS, 'Completed'),
        (CANCELLED_STATUS, 'Cancelled'),              
    )

    CUSTOMER_CHOICES = (
            ('personal', 'Personal'),
            ('entreprise', 'Entreprise'),
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Personal, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=20, choices=SIZES, default=MEDIUM_SIZE)
    quantity = models.IntegerField(default=1)
    photo = models.ImageField(upload_to="job/photos/")
    status = models.CharField(max_length=20, choices=STATUSES, default=CREATING_STATUS)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
