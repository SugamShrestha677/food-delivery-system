from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsCustomer]

    def get_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        return cart

    def list(self, request):
        cart = self.get_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_item(self, request):
        cart = self.get_cart(request)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            menu_item = serializer.validated_data['menu_item']
            quantity = serializer.validated_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
            if not created:
                cart_item.quantity += quantity
            cart_item.save()
            return Response(CartItemSerializer(cart_item).data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['patch'])
    def update_item(self, request):
        cart = self.get_cart(request)
        try:
            item = CartItem.objects.get(cart=cart, menu_item__id=request.data['menu_item_id'])
            item.quantity = request.data['quantity']
            item.save()
            return Response(CartItemSerializer(item).data)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Item not found in cart.'}, status=404)

    @action(detail=False, methods=['delete'])
    def remove_item(self, request):
        cart = self.get_cart(request)
        try:
            item = CartItem.objects.get(cart=cart, menu_item__id=request.data['menu_item_id'])
            item.delete()
            return Response({'detail': 'Item removed.'})
        except CartItem.DoesNotExist:
            return Response({'detail': 'Item not found.'}, status=404)
