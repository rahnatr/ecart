from django.db import models
from ecart.customers.models import Customer
from ecart.products.models import Product


# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    delete_status=models.IntegerField(choice=DELETE_CHOICE,default=LIVE)
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,'Order_Processed'),(ORDER_DELIVERED,'Order_Delivered'),(ORDER_REJECTED,'Order_Rejected'))
    order_status=models.IntegerField(choice=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='Orders')    
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

   
    