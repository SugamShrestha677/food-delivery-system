from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Delivery, DeliveryPerson
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DeliverySerializer, DeliveryPersonSerializer
from rest_framework.permissions import AllowAny
from apps.notifications.models import Notification  # 🔔 Import Notification
from rest_framework.generics import CreateAPIView
from .serializers import DeliveryPersonRegisterSerializer
from apps.accounts.models import Users
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from.permission import *



class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [AllowAny]  # Adjust based on your auth

    def perform_create(self, serializer):
        delivery = serializer.save()
        delivery_person_user = delivery.delivery_person.user  # Assuming FK to Users model
        
        # 🔔 Create notification for delivery person
        Notification.objects.create(
            user=delivery_person_user,
            message=f"You've been assigned a delivery: Order #{delivery.order.id}"
        )

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer
    permission_classes = [AllowAny]



class DeliveryPersonRegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = DeliveryPersonRegisterSerializer
    permission_classes = [AllowAny]


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

class DeliveryPersonDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDeliveryPerson]

    def get(self, request):
        return Response({"message": f"Welcome {request.user.username} to the restaurant dashboard"})

class DeliveryPersonProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        deliverPerson = get_object_or_404(DeliveryPerson, user=request.user)
        serializer=DeliveryPersonSerializer(deliverPerson)
        return Response(serializer.data)
    def put(self, request):
        deliverPerson = get_object_or_404(DeliveryPerson, user=request.user)
        serializer=DeliveryPersonSerializer(deliverPerson,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)