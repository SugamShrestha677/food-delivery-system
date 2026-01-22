# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import *
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.conf import settings
# from django.conf.urls.static import static

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', TokenObtainPairView.as_view(), name='login'),
#     path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
#     path('password-reset-confirm/<int:uid>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('me/', UserProfileView.as_view(), name='user-profile'),


# ]

#     # path('users/', UserViewSet.as_view(), name='users'),
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from .import views

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='custom_login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<int:uid>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserProfileView.as_view(), name='user-profile'),
]

    # path('users/', UserViewSet.as_view(), name='users'),
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)