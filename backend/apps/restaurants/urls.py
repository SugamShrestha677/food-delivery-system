from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'restaurantList', ViewRestaurantSet, basename='users')
router.register(r'menu-items', MenuItemViewSet, basename='menu-items')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RestaurantRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('<int:id>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurant_list/', RestaurantListAPIView.as_view(), name='restaurant-list'),

]