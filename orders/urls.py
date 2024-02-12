from django.urls import path
from .views import add_to_cart
from . import views

urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order', views.view_orders, name='order'),
]