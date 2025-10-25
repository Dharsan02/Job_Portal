from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login ,logout as auth_logout,authenticate
from .models import *
from companypage.models import *


def signup(request):
  context={
    'error':''
  }
  if request.method=='POST':
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('pass')
    mobile_no=request.POST.get('mobile_no')
    if User.objects.filter(email=email).exists():
      context={
        'error':'Email ID already exists'
      }
      return render(request,'signup.html',context)
    else:
      new_user=User.objects.create_user(username=name,email=email,password=password,mobile_no=mobile_no)
      return redirect('login')
  return render(request,'signup.html',context)
def login(request):
  context={
    'error':''
  }
  if request.method=="POST":
    email=request.POST.get('email')
    password=request.POST.get('pass')

    user_check=authenticate(email=email,password=password)
    if user_check is not None:
      auth_login(request,user_check)
      return redirect('home')
    else:
      context={
        'error':'invalid email_id or password'
      }
      return render(request,'login.html',context)
  return render(request,'login.html',context)

def logout(request):
  auth_logout(request)
  return redirect('login')
# Create your views here.

def company_signup(request):
  context={
   'error':''
  }
  if request.method=="POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    mobile_no=request.POST.get('mobile_no')
    location=request.POST.get('location')
    industry_type=request.POST.get('industry_type')
    password=request.POST.get('password')
    if User.objects.filter(email=email).exists():
     context={
       'error':'Email already exists'
      }
     return render(request,'company_signup.html',context)
    else:
      new_user=User.objects.create_user(username=name,email=email,mobile_no=mobile_no,location=location,industry_type=industry_type,password=password)
      return redirect('company_login')
  return render(request,'company_signup.html',context)
 

def company_login(request):
  context={
    "error":''
  }
  if request.method=="POST":
    email=request.POST.get('email')
    password=request.POST.get('password')

    user_check=authenticate(email=email,password=password)
    if user_check is not None:
      auth_login(request,user_check)
      return redirect('hire')
    else:
      context={
        "error":"invalid email or password"
      }
      return render(request,'company_login.html',context)
  return render(request,'company_login.html',context)
  

def company_logout(request):
  logout(request)
  redirect('company_login')  
    
   