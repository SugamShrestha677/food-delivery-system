import datetime
from django.db import models
from apps.accounts.models import Users
from django.contrib.auth.hashers import make_password

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    restaurant_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    contact = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)
    delivery_fees = models.IntegerField(default=0)
    cuisine_type = models.CharField(max_length=100,default="null")
    logo = models.ImageField(upload_to='restaurant_logos/', null=True, blank=True)
    
    def __str__(self):
        return self.restaurant_name or f"Restaurant {self.id}"

    def get_username(self):
        return self.user.username if hasattr(self, 'user') and self.user else 'Not linked'
    

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    items = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    estimated_time = models.TimeField(auto_now=False, auto_now_add=False,default=datetime.time(0, 5))
    category = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.items
    
# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('accepted', 'Accepted'),
#         ('preparing', 'Preparing'),
#         ('out_for_delivery', 'Out for Delivery'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#     ]

#     customer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orders')
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
#     delivery_address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order #{self.id} - {self.customer}"
    

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)  # Single unit price

#     def __str__(self):
#         return f"{self.quantity} x {self.menu_item}"