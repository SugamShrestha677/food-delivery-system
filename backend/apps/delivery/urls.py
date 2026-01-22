from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *

router = DefaultRouter()
router.register(r'deliveries', DeliveryViewSet)
router.register(r'delivery-persons', DeliveryPersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', DeliveryPersonRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', DeliveryPersonProfileView.as_view(), name='user-profile'),
]
