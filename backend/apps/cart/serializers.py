from rest_framework import serializers
from .models import Cart, CartItem
from apps.restaurants.models import MenuItem  # ✅ Updated

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'items', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source='menu_item', write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'menu_item', 'menu_item_id', 'quantity', 'total_price']
        read_only_fields = ['total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
        read_only_fields = ['user', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()
