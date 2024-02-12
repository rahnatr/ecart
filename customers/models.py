from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=(
        (LIVE,'Live'),
        (DELETE,'Delete')
    )
    name=models.CharField(max_length=200,default='user')    
    address=models.CharField(max_length=500) 
    phonenumber=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')   
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    craeted_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self)-> str:
        return self.name
        # return self.user.username    #it is also correct

    

   
    