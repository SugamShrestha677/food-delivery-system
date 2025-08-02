from django.urls import path
from .views import CartViewSet

cart_list = CartViewSet.as_view({'get': 'list'})
add_item = CartViewSet.as_view({'post': 'add_item'})
update_item = CartViewSet.as_view({'patch': 'update_item'})
remove_item = CartViewSet.as_view({'delete': 'remove_item'})

urlpatterns = [
    path('', cart_list, name='cart-detail'),
    path('add/', add_item, name='cart-add-item'),
    path('update/', update_item, name='cart-update-item'),
    path('remove/', remove_item, name='cart-remove-item'),
]
