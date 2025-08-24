from django.shortcuts import get_object_or_404, render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.generics import RetrieveAPIView
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class RestaurantRegisterView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantRegisterSerializer
    permission_classes = [AllowAny]

class ViewRestaurantSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = GetRestaurantSerializer
    permission_classes = [AllowAny]


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'  # default is 'pk', but specifying for clarity

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def perform_create(self, serializer):
#         serializer.save(customer=self.request.user)  # assuming user is logged in



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow only restaurant owners to POST (create).
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return hasattr(request.user, 'restaurant')  # check if user is a restaurant
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.restaurant.user == request.user


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def get_queryset(self):
        user = self.request.user
        try:
            restaurant = Restaurant.objects.get(user=user)  # or .get(pk=user.pk) depending on your model
        except Restaurant.DoesNotExist:
            return MenuItem.objects.none()  # return empty queryset if restaurant not found

        return MenuItem.objects.filter(restaurant=restaurant)



    def perform_create(self, serializer):
        restaurant = getattr(self.request.user, 'restaurant', None)
        if not restaurant:
            raise PermissionDenied("Only restaurant owners can add menu items.")
        serializer.save(restaurant=restaurant)


# from django.shortcuts import render

# def restaurant_list(request):
#     return render(request, 'restaurant/list.html')




# # apps/restaurants/views.py
# from django.http import JsonResponse
# from .models import Restaurant

# def restaurant_list(request):
#     data = []
#     for r in Restaurant.objects.all():
#         if r.user:
#             data.append({
#                 "id": r.id,
#                 "name": r.restaurant_name,
#                 "owner": r.user.username,
#             })
#     return JsonResponse(data, safe=False)
class RestaurantListAPIView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = GetRestaurantSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}  # Needed to generate full image URL
    

from django.contrib.auth import logout, authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
# Custom login view with role-based checks
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            # Get the user from the request
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            
            if user:
                print(f"DEBUG: API Login - User {user.username} has role: {user.role}")
                
                # Add role information to the response
                response.data['role'] = user.role
                response.data['username'] = user.username
                
                # Also log the user in via Django session for compatibility
                from django.contrib.auth import login
                login(request, user)
        
        return response
    


# views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permission import IsRestaurantOwner

class RestaurantDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsRestaurantOwner]

    def get(self, request):
        return Response({"message": f"Welcome {request.user.username} to the restaurant dashboard"})


class RestaurantProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurant = get_object_or_404(Restaurant, user=request.user)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request):
        restaurant = get_object_or_404(Restaurant, user=request.user)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
