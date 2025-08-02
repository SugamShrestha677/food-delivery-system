from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    # readonly_fields = ['total_price']
    autocomplete_fields = ['menu_item']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'total_price_display']
    inlines = [CartItemInline]
    search_fields = ['user__username']
    readonly_fields = ['created_at']

    def total_price_display(self, obj):
        return obj.total_price()
    total_price_display.short_description = 'Total Price'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'menu_item', 'quantity', 'total_price']
    list_filter = ['cart']
    search_fields = ['menu_item__name', 'cart__user__username']
