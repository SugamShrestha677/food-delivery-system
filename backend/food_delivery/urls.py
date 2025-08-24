# """
# URL configuration for food_delivery project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include
# from . import views

# from django.conf import settings
# from django.conf.urls.static import static
# from django.http import JsonResponse
# def test_connection(request):
#     client_time = request.GET.get('time', None)
#     return JsonResponse({
#         'status': 'success',
#         'message': 'Backend is connected',
#         'received_time': client_time,
#         'server_processed': True
#     })



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home),
#     path('restaurantcheck/', views.restaurant_template_view),
#     path('restaurant/dashboard/', views.restaurant_dashboard),
#     path('restaurant/menu/', views.menu),
#     path('restaurant/order/', views.order),
#     path('restaurant/profile/', views.profile),
#     path('restaurant/signin/', views.restaurant_signin,name='restaurant_signin'),
#     path('customer/', views.customer,name='restaurant_signin'),
#     path('signin/', views.restaurant_session_login, name='restaurant-signin'),
#     path('dashboard/', views.restaurant_dashboard, name='restaurant-dashboard'),
#     path('customer/signin/', views.customer_signin,name='customer_signin'),
#     path('deliveryperson/signin/', views.deliveryperson_signin,name='deliveryperson_signin'),
#     path('deliveryperson/dashboard/', views.deliveryperson_dashboard,name='deliveryperson_dashboard'),
#     path('restaurant/', views.restaurant),
#     # path('',views.user_sign),
#     # path('restaurant/',views.restaurant_sign),
#     # path('home/',views.dashboard),
#     path('api/auth/', include("apps.accounts.urls")),
#     path('api/restaurant/', include("apps.restaurants.urls")),
#     path('api/delivery/', include("apps.delivery.urls")),
#     path('api/notifications/', include('apps.notifications.urls')),
#     path('api/', include('apps.orders.urls')),
#     path('api/cart/', include('apps.cart.urls')),
#     path('api/test/', test_connection, name='test-connection'),
#     path('profile/', views.profile, name='profile'),
#     # path('test/', views.test_page, name='test-page'),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path, include

from apps.accounts.views import CustomerDashboardAPIView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Authentication
    # path('signin/', views.signin, name='signin'),
    path('restaurant/signin/', views.restaurant_signin, name='restaurant_signin'),
    path('customer/signin/', views.customer_signin, name='customer_signin'),
    path('deliveryperson/signin/', views.deliveryperson_signin, name='deliveryperson_signin'),

    # Dashboards
    path('restaurant/dashboard/', views.restaurant_dashboard, name='restaurant_dashboard'),
    path('customer/dashboard/', views.customer_dashboard , name='customer_dashboard'),
    path('deliveryperson/dashboard/', views.deliveryperson_dashboard, name='deliveryperson_dashboard'),

    # Restaurant Views
    path('restaurantcheck/', views.restaurant_template_view),
    path('restaurant/menu/', views.menu),
    path('restaurant/order/', views.order),
    path('restaurant/profile/', views.profile),
    path('restaurant/', views.restaurant),
    path('customer_profile/',views.customer_profile,name='customer_profile'),
    path('about/', views.about_us, name='about_us'),

    path('logout/', views.signout, name='logout'),


    # API Endpoints
    path('api/auth/', include("apps.accounts.urls")),
    path('api/customer/dashboard/', CustomerDashboardAPIView.as_view(), name='customer_dashboard_api'),
    path('api/restaurant/', include("apps.restaurants.urls")),
    path('api/delivery/', include("apps.delivery.urls")),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/', include('apps.orders.urls')),
    path('api/cart/', include('apps.cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
