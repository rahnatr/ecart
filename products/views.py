from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):    
    return render(request,'products.html')

def about(request):    
    return render(request,'about.html')

def contact(request):    
    return render(request,'contact.html')

def account(request):    
    return render(request,'account.html')

def product_detail(request):    
    return render(request,'product_details.html')

def cart(request):    
    return render(request,'cart.html')


