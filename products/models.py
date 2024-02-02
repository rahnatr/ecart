from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_STATUS=((LIVE,'Live'),(DELETE,'Delete'))
    item_name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to='/media')
    description=models.CharField(max_length=500)
    delete_choice=models.IntegerField(choice=DELETE_STATUS,default=LIVE)
    priority=models.IntegerField(default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self)-> str:
        return self.Item_Name