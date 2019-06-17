from django.shortcuts import render
from .models import ShopUser

# Create your views here.

def register(request):
    return render(request, 'authapp/register.html')

def login(reauest):
    return render(reauest, 'authapp/login.html')

def edit(request):
    return render(request, 'authapp/edit.html')

def logout(request):
    return render(request, 'authapp/logout.html')