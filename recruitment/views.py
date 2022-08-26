import pdb
from django.shortcuts import render, redirect
from .forms import AppForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from .models import JobDescription


def index(request):
    form = UserForm()
    context = { 'form': form}
    return render(request, 'index.html', context) 


def register(request):  
    # pdb.set_trace()
    if request.method == 'POST':  
        form = UserForm(request.POST)  
        if form.is_valid():  
            form.save() 
            messages.success(request, "your account has been created successfully")
            return redirect('/')
   
    else:  
        form = UserForm()  
    context = {  
        'form':form  
    }      
    return render(request, 'register.html', context)  


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
                
            else:
                messages.error(request,"Invalid username or password.")
                return redirect('/')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logOut(request):
    messages.success(request,"logged out successfully")
    logout(request)
    
    return redirect('/')

def JobDescriptionView(request):
    return render(request, 'jd.html')
    

def applied_job(request):
    
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppForm()
    context = {'form':form}
    return render(request,'form.html',context)    