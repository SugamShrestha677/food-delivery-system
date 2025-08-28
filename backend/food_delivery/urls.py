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
