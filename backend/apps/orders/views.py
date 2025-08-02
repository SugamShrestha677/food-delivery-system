from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from apps.notifications.models import Notification  # 🔔 Import Notification
from rest_framework.permissions import AllowAny
from .models import OrderItem
from .serializers import OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Order
from apps.notifications.models import Notification
from rest_framework.exceptions import PermissionDenied


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]  # Adjust if needed

    def perform_create(self, serializer):
        order = serializer.save(customer=self.request.user)  # Save order with logged-in user
        
        # 🔔 Create notification for the customer
        Notification.objects.create(
            user=self.request.user,
            message=f"Your order #{order.id} has been placed successfully!"
        )
class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']




class CancelOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):  # order_id from URL
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

        if order.customer != request.user:
            raise PermissionDenied('You are not allowed to cancel this order.')

        if order.status == 'cancelled':
            return Response({'error': 'Order is already cancelled.'}, status=status.HTTP_400_BAD_REQUEST)

        if order.status == 'delivered':
            return Response({'error': 'Delivered orders cannot be cancelled.'}, status=status.HTTP_400_BAD_REQUEST)

        order.status = 'cancelled'
        order.save()

        Notification.objects.create(
            user=request.user,
            message=f"Your order #{order.id} has been cancelled."
        )

        return Response({'message': f"Order #{order.id} cancelled successfully."}, status=status.HTTP_200_OK)