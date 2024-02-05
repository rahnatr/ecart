from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index),
    path('Products',views.products,name='products')
   
]

