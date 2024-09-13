from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


def user_login(request):
    next_url = request.GET.get('next')
    if next_url is None:
        next_url = reverse('app:dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form, 'next':next_url})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('app:index')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('password-change-success') 
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/password_change.html', {'form':form})

def password_change_success(request):
    return render(request, 'registration/password_change_success.html')
