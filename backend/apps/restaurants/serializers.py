from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.core.mail import send_mail

restaurant_token_generator = default_token_generator


Users = get_user_model()

class RestaurantRegisterSerializer(serializers.ModelSerializer):

    # These fields are for user creation
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    role = serializers.CharField(default='restaurant_owner', write_only=True)

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'address', 'contact', 'delivery_fees','logo',
                  'username', 'password', 'email', 'role']


    
    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        role = validated_data.pop('role', 'restaurant_owner')


        print("Creating user with:", username, password, email, role)
        # Create the user securely
        try:
            user = Users.objects.create_user(
                username=username,
                password=password,
                email=email,
                role=role,
                is_active=True
            )
            print("✅ User created:", user.username)
        except Exception as e:
            print("❌ Error creating user:", str(e))
            raise serializers.ValidationError(f"Failed to create user: {str(e)}")


        print("Creating user with:", username, password, email, role)

        if not user:
            raise serializers.ValidationError("User creation failed; cannot create restaurant without a user.")
        # Create and link the restaurant
        restaurant = Restaurant.objects.create(user=user, **validated_data)
        print("Restaurant created:", restaurant.restaurant_name, restaurant.user.username)
        return restaurant
    

class GetRestaurantSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'username', 'restaurant_name', 'address', 'contact', 'logo_url']

    def get_logo_url(self, obj):
        request = self.context.get('request')
        if obj.logo and hasattr(obj.logo, 'url'):
            return request.build_absolute_uri(obj.logo.url)
        return None




        
class RestaurantDetailSerializer(serializers.ModelSerializer):
    menu_items = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_name', 'address', 'contact', 'menu_items']  # removed 'user'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ['restaurant']  # auto-set from logged-in user








# class OrderItemSerializer(serializers.ModelSerializer):
#     menu_item_name = serializers.CharField(source='menu_item.items', read_only=True)

#     class Meta:
#         model = OrderItem
#         fields = ['id', 'menu_item', 'menu_item_name', 'quantity' ]

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True, write_only=True)
#     ordered_items = OrderItemSerializer(source='items', many=True, read_only=True)  # use related_name='items' in model

#     class Meta:
#         model = Order
#         fields = ['id', 'customer', 'restaurant', 'delivery_address', 'status', 'created_at', 'items','ordered_items']
#         read_only_fields = ['id', 'status', 'created_at']

#     def create(self, validated_data):
#         items_data = validated_data.pop('items')
#         order = Order.objects.create(**validated_data)

#         total = 0
#         for item_data in items_data:
#             menu_item = item_data['menu_item']
#             quantity = item_data['quantity']
#             price = menu_item.price
#             total += price * quantity
#             OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity, item_price=price)

#         order.total_price = total
#         order.save()
#         return order