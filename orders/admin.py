from django.contrib import admin
from orders.models import Order,OrderedItem
# Register your models here.
# admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'total_price', 'order_status', 'created_at', 'updated_at']
    list_filter = ['owner','order_status', 'created_at', 'updated_at']
    search_fields = ['id', 'owner']  # Assuming owner is a User model related field

admin.site.register(Order, OrderAdmin)