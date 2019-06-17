from django.shortcuts import render, HttpResponseRedirect
from .models import ShopUser
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse

# Create your views here.

def register(request):
    return render(request, 'authapp/register.html')

def login(request):
    if request.method == 'POST':
        unm = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=unm, password=password)
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/login.html')


class EditView(UpdateView):
    pass

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
