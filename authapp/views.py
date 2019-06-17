from django.shortcuts import render
from .models import ShopUser
from django.views.generic.edit import UpdateView

# Create your views here.

def register(request):
    return render(request, 'authapp/register.html')

def login(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'authapp/login.html')


class EditView(UpdateView):
    pass

def logout(request):
    return render(request, 'authapp/logout.html')