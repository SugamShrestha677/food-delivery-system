from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/<int:order_id>/cancel/', CancelOrderView.as_view(), name='cancel-order'),
]