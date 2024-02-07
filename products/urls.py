from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('Products',views.products,name='products'),
    path('About',views.about,name='about'),
    path('Contact',views.contact,name='contact'),
    path('Account',views.account,name='account'),
    path('Product_details',views.product_detail,name='product_detail'),
    path('Cart',views.cart,name='cart'),
]

