from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        # Login user
        return
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Register user
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard')
