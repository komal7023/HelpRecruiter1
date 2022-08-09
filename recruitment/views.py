from django.shortcuts import render, redirect
from .models import User, JobDescription, JobApplicant
from .forms import UserForm

def index(request):
    users = User.objects.order_by('id')
    form = UserForm()
    context = {'users' : users, 'form' : form}
    return render(request, 'index.html', context)


