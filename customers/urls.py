
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
import products
from . import views


urlpatterns = [
     
    path('account',views.account,name='account'),
    path('logout',views.sign_out,name='logouturl'),   
    
   
]
