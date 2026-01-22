from rest_framework import serializers
from apps.notifications.serializers import NotificationSerializer
from .models import *
from .utils import user_password_reset_token
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse


class UserSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True, read_only=True)
    class Meta:
        model = Users
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'role', 'phone', 'address', 'photo']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # remove password from dictionary
        user = Users(**validated_data)             # create user instance
        user.set_password(password)    # hash password
        user.is_active = True               
        user.save()
        return user
    


# Forget password feature

User = get_user_model()

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        users = User.objects.filter(email=value)
        if not users.exists():
            raise serializers.ValidationError("No user associated with this email.")
        
        for user in users:
            if user.is_superuser:
                raise serializers.ValidationError("Admin password reset is not allowed.")
        
        return value

    def save(self):
        request = self.context.get('request')
        email = self.validated_data['email']
        users = User.objects.filter(email=email)

        for user in users:
            token = user_password_reset_token.make_token(user)
            uid = user.pk
            reset_url = request.build_absolute_uri(
                reverse('password-reset-confirm', kwargs={'uid': uid, 'token': token})
            )

            send_mail(
                subject="Password Reset Request",
                message=f"Click the link to reset your password: {reset_url}",
                from_email=None,
                recipient_list=[email],
            )


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.IntegerField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            user = User.objects.get(pk=attrs['uid'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user ID.")

        if not user_password_reset_token.check_token(user, attrs['token']):
            raise serializers.ValidationError("Invalid or expired token.")
        
        if user.is_superuser:
            raise serializers.ValidationError("Admin password reset is not allowed.")
        
        attrs['user'] = user
        return attrs

    def save(self):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])

        user.save()
