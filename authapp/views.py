from django.shortcuts import render
from .models import ShopUser
from django.views.generic.edit import UpdateView

# Create your views here.

def register(request):
    return render(request, 'authapp/register.html')

def login(reauest):
    return render(reauest, 'authapp/login.html')

class EditView(UpdateView):
    pass

def logout(request):
    return render(request, 'authapp/logout.html')