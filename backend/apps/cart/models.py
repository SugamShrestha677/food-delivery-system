from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from apps.restaurants.models import MenuItem  # ✅ Updated

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s Cart"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # ✅ Updated
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['cart', 'menu_item']  # ✅ Updated

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.items}"  # ✅ Updated

    def total_price(self):
        return self.quantity * self.menu_item.price  # ✅ Updated
