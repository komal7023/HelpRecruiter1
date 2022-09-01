import pdb
from django.shortcuts import render, redirect
from .forms import ApplicationForm, UserForm, ApplicantForm, JobDescriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from .models import JobApplication, JobDescription


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

def log_out(request):
    messages.success(request,"logged out successfully")
    logout(request)
    
    return redirect('/')

def detail_view(request,pk):
    jobDescription=JobDescription.objects.filter(id=pk)
    context = {"jds":jobDescription}
    return render(request, 'jd.html', context)    

def job_description_view(request):
    jobDescription = JobDescription.objects.all()

    context = {"jds":jobDescription}
    return render(request, 'index.html', context)
    

def applied_job(request):
    
    if request.method == 'POST':
        pdb.set_trace()
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('applicants/')
    else:
        form = ApplicationForm()
    context = {'form':form}
    return render(request,'form.html',context)    

def application_view(request):

    if request.method == 'POST':
        pdb.set_trace()

        form = ApplicantForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ApplicantForm(user=request.user)
    context = {'form':form}
    return render(request,'applicant.html',context)
