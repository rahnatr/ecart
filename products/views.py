from django.shortcuts import get_object_or_404, render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products,
        }    
    return render(request,'index.html',context)

def products(request):    
    page=1
    if request.GET:
        page=request.GET.get('page',1)    
    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    
    context={
       
        'products':product_list}
    return render(request,'products.html',context)



def about(request):    
    return render(request,'about.html')

def contact(request):    
    return render(request,'contact.html')

def product_detail(request,pk):  
    
    selected_product=Product.objects.get(pk=pk)  
    context={
        'selected_product':selected_product
    }
    return render(request,'product_details.html',context)

def cart(request):    
    return render(request,'cart.html')


