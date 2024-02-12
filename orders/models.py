from django.db import models
from customers.models import Customer
from products.models import Product


# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,'Order_Processed'),(ORDER_DELIVERED,'Order_Delivered'),(ORDER_REJECTED,'Order_Rejected'))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)    
    owner = models.ForeignKey(Customer,blank=True, null=True, on_delete=models.SET_NULL, related_name='Orders')   
    total_price = models.FloatField(default=0) 
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self)-> str:
         return "order-{}-{}".format(self.id,self.owner.name)
    
    

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,blank=True, null=True,on_delete=models.SET_NULL,related_name='added_carts')
    quantity = models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

   
    