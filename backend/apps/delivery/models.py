from django.db import models
from apps.accounts.models import Users
from apps.orders.models import Order
from apps.restaurants.models import Restaurant

class DeliveryPerson(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    license_number = models.CharField(max_length=120)
    fullname = models.CharField(max_length=120,default="unknown")
    vehicle_type = models.CharField(max_length=20, default="2 wheeler")  # Fixed default
    vehicle_number = models.CharField(max_length=20)
    license_photo = models.ImageField(upload_to='license_photos/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username  #  uses related user's username
 
class Delivery(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed Delivery'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')
    delivery_person = models.ForeignKey(
        DeliveryPerson, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='deliveries'  # Added related name for reverse access
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    delivery_address = models.TextField()
    estimated_time = models.CharField(max_length=50, default="30-40 minutes")
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"Delivery for Order #{self.order.id}"
