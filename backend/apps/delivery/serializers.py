from rest_framework import serializers
from wtforms import ValidationError
from apps.accounts.serializers import UserSerializer
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['status']


class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = ['id', 'user', 'phone', 'vehicle_number', 'is_available']
        # Optional: if user is not sent via request and you want to use the current user
        # extra_kwargs = {'user': {'read_only': True}}

    # Optional: for setting the user from request 
    def create(self, validated_data):
        return DeliveryPerson.objects.create(**validated_data)



class DeliveryPersonRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    license_photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = DeliveryPerson
        exclude = ['user', 'is_approved', 'is_available']

    def validate(self, attrs):
        User = get_user_model()
        username = attrs.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": "Username already exists."}
            )
        return attrs

    def create(self, validated_data):
        User = get_user_model()
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            role='driver'
        )
        # Handle license_photo separately
        license_photo = validated_data.pop('license_photo', None)
        delivery_person = DeliveryPerson.objects.create(
            user=user, 
            license_photo=license_photo,
            **validated_data
        )
        return delivery_person
    



User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD  # usually "username" or "email"

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }

        self.user = authenticate(**authenticate_kwargs)

        if self.user is None or not self.user.is_active:
            raise serializers.ValidationError('No active account found with the given credentials')

        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        return data