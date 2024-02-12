from typing import Self
from django.shortcuts import render, redirect
from orders.models import Order, OrderedItem
from django.contrib import messages
from products.models import Product
from customers.models import Customer
from orders.models import Order
from products.views import product_detail
from . import views
import orders
# Create your views here.

def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user   
            if hasattr(user,'customer_profile'):  
                customer = user.customer_profile
                quantity = request.POST.get('quantity')
                product_id = request.POST.get('product_id')
                if not quantity or not product_id:
                    messages.error(request, "Invalid request. Please specify the quantity and product.")
                    return redirect('home')  # Redirect to home or another appropriate page
            
                try:
                    product = Product.objects.get(pk=product_id)
                except Product.DoesNotExist:
                    messages.error(request, "Invalid product. Please select a valid product.")
                    return redirect('home')  # Redirect to home or another appropriate page
            
                if not customer:
                    messages.error(request, "You need to create a customer profile to add items to your cart.")
                    return redirect('login')  # Redirect to the profile creation page
            
                cart_obj, created = Order.objects.get_or_create(
                    owner=customer,
                    order_status=Order.CART_STAGE
                )
            
                ordered_item, created = OrderedItem.objects.get_or_create(
                    product=product,
                    owner=cart_obj,
                    defaults={'quantity': quantity}
                )             
            
                if created:
                    ordered_item.quantity=quantity
                    ordered_item.save()
                else:
                    ordered_item.quantity += int(quantity)
                    ordered_item.save()  
            
            # if not created:
            #     # Update quantity if item already exists
            #     ordered_item.quantity += int(quantity)
            #     ordered_item.save()
            
            #subtotal            
            
                return redirect('products')
            else:
                messages.error(request, "You need to be logged in to add items to your cart.")
                return redirect('account')  # Redirect to the login page if the user is not authenticated
        else:
            messages.error(request, "Invalid request method.")
            return redirect('home')  # Redirect to home or another appropriate page   

def show_cart(request):
    if request.method == 'POST':
        # If a POST request is made, it might indicate that the user is updating the cart.
        # You can handle cart updates here if needed, but typically, displaying the cart is associated with GET requests.
        pass
    else:
        # For GET requests, retrieve the user's customer profile and their cart
        user = request.user
        if hasattr(user, 'customer_profile'):
            customer = user.customer_profile
            cart_obj, created = Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            context = {'cart': cart_obj}
            return render(request, 'cart.html', context)
        else:
            # If the user does not have a customer profile, you might want to handle this case differently
            return redirect('login')  # Redirect to the profile creation page or another appropriate page
        
def remove_from_cart(request, pk):
    delete_item=OrderedItem.objects.get(pk=pk)
    
    if delete_item.quantity > 1:
        delete_item.quantity -= 1
        delete_item.save()
    else:
        delete_item.delete()
    return redirect('cart')

def checkout(request,):
     if request.method == 'POST':           
            try:
                user = request.user       
                customer = user.customer_profile            
                total = float(request.POST.get('total'))
                order_obj = Order.objects.get(
                    owner=customer,
                    order_status=Order.CART_STAGE
                )
                if order_obj:
                    order_obj.order_status = Order.ORDER_CONFIRMED
                    order_obj.total_price = total
                    order_obj.save()
                    status_message="Your order is proccessed"
                    messages.success(request,status_message)
                else:
                    status_message="Your order unable to proccessed"
                    messages.error(request,status_message)
            except Exception as e:
                status_message="Your order unable to proccessed"
                messages.error(request,status_message)
            return redirect('order')
      
def view_orders(request):    
    if request.user.is_authenticated:
        
            user = request.user
            if hasattr (user,'customer_profile'):
                customer = user.customer_profile
                all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
                context={
                    'orders':all_orders
                }
                
                return render(request,'order.html',context)
            else:
                print("No customer profile found for the user")
    else:
        print("User is not authenticated")            
       
        
   
                
            

