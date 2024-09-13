from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})

def password_change_success(request):
    return render(request, 'registration/password_change_success.html')