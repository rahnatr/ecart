

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.urls import reverse
from . models import Customer
from django.contrib import messages

# Create your views here.
def sign_out(request):
    logout(request)   
    return redirect('home')
    
def account(request):  
    context={ }
    error_message = None
    if request.method == 'POST' and 'btn_register' in request.POST:
        context['register']=True
        try:                   
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phonenumber = request.POST.get('phonenumber')
            
            # Check if username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                raise Exception("Duplicate username or email")
            
            #create user account
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password                
            )
           
            #create customer account
            customer=Customer.objects.create(
                name=user,
                user=user,
                phonenumber=phonenumber,
                address=address
            )            
            # Redirect to home page after successful registration 
            #return redirect("home")
            messages.success(request,"User registered successfully")          
        except Exception as e:
            error_message="Duplicate username or emailid"
            messages.error(request,error_message)
    if request.method == 'POST' and 'btn_login' in request.POST:
        context['register']=False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message="Invalid credentials"
            messages.error(request,error_message)
    
    return render(request,'account.html',context)
    
    
