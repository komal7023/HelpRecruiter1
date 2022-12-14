from django.shortcuts import render, redirect
from .forms import UserForm, ApplicantForm
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
    if request.method == 'POST':  
        form = UserForm(request.POST)  
        if form.is_valid():  
            form.save() 
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
    logout(request)
    return redirect('/') 

def detail_view(request,pk):
    jobDescription=JobDescription.objects.filter(id=pk)
    context = {"jds":jobDescription}
    return render(request, 'job_description.html', context)    

def job_description_view(request):
    jobDescription = JobDescription.objects.all()
    context = {"jds":jobDescription}
    return render(request, 'index.html', context)
    
def applied_job(request):
    appliedJob = JobApplication.objects.all()
    context={"jobs":appliedJob}
    return render(request,'applied_job.html',context)

def application_view(request,pk): 
    if request.method == 'POST':
        form = ApplicantForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ApplicantForm(user=request.user, job_description = pk)
    context={'form':form}
    return render(request,'application_form.html',context)     


             


