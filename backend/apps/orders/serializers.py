from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password 

User = get_user_model()


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.items', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity' ]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    ordered_items = OrderItemSerializer(source='items', many=True, read_only=True)  # use related_name='items' in model

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'delivery_address', 'status', 'created_at', 'items','ordered_items']
        read_only_fields = ['id', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total = 0
        for item_data in items_data:
            menu_item = item_data['menu_item']
            quantity = item_data['quantity']
            price = menu_item.price
            total += price * quantity
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity, item_price=price)

        order.total_price = total
        order.save()
        return order