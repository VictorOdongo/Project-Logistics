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

    # CUSTOMER_CHOICES = (
    #         ('personal', 'Personal'),
    #         ('entreprise', 'Entreprise'),
    #     )
    
    # step 1
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
    
    # step 2
    pickup_address = models.CharField(max_length=255, blank=True)
    pickup_lat = models.FloatField(default=0.0)
    pickup_lng = models.FloatField(default=0.0)
    pickup_name = models.CharField(max_length=255, blank=True)
    pickup_phone = models.CharField(max_length=255, blank=True)
    
    # step 3
    delivery_address = models.CharField(max_length=255, blank=True)
    delivery_lat = models.FloatField(default=0.0)
    delivery_lng = models.FloatField(default=0.0)
    delivery_name = models.CharField(max_length=255, blank=True)
    delivery_phone = models.CharField(max_length=255, blank=True)
    
    # step 4
    duration = models.IntegerField(default=0)
    distance = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.description
    
class Transaction(models.Model):
    stripe_payment_intent_id = models.CharField(max_length=255, unique=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.stripe_payment_intent_id
    
