from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from app.models import contact
# Create your views here.
def index (request):
    return render(request,"index.html")

def about (request):
    return render (request,"about.html")    

def services (request):
    return render (request,"services.html") 

def project (request):
    return render (request,"project.html")   

def blog (request):
    return render (request,"blog.html")

def contact (request):
    return render (request,"contact.html")  

def reg (request):
    return render (request,"reg.html")     

def regdata(request):
    fname=request.POST["fname"] 
    lname=request.POST["lname"] 
    email=request.POST["email"] 
    uname=request.POST["username"] 
    password=request.POST["password"] 
    confirm=request.POST["cpassword"]
    reg=User(first_name=fname,last_name=lname,email=email,username=uname,password=password) 
    reg.set_password(reg.password)
    reg.save()
    return redirect('register')    

def login(request):
    return render(request,"login.html") 

def userlogin(request):
    username=request.POST["username"] 
    password=request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request,user)
        messages.error(request, 'welcome to our website') 
        return redirect('home')

    else:
        messages.error(request, 'userame and password does\'nt match')

        return redirect('login') 

def logoutuser(request):
    logout(request)
    return redirect('login') 

def csave(request):
    username=request.POST["uname"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    subject=request.POST["subject"]
    message=request.POST["message"]
    conts = contact(username=username,email=email,phone=phone,subject=subject,message=message)
    conts.save()
    return redirect('home')
