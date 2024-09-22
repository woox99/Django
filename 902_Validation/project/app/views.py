from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)

    # if form doesn't pass validation
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        form_data = {
            'name' : request.POST['name'],
            'email' : request.POST['email'],
            'password' : request.POST['password'],
            'confirm' : request.POST['confirm'],
        }
        return render(request, 'index.html', form_data)
    
    # Else if form passes validation
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    name = request.POST['name']
    email = request.POST['email']
    User.objects.create(name=name, email=email, password=pw_hash)

    return redirect('/dashboard')

def login(request):
    errors = User.objects.validate_login(request.POST)

    # if login doesn't pass validation
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        form_data = {
            'email' : request.POST['email'],
            'password' : request.POST['password'],
        }
        return render(request, 'index.html', form_data)
    return redirect('/dashboard')