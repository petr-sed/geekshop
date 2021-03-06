from django.shortcuts import render, HttpResponseRedirect
from .models import ShopUser
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from .forms import ShopUserRegisterForm, ShopUserEditForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    context = {'form': register_form}
    return render(request, 'authapp/register.html', context)

def login(request):

    if request.method == 'POST':
        unm = request.POST.get('login')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = auth.authenticate(username=unm, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('main'))
    return render(request, 'authapp/login.html', {'next': request.GET.get('next')})


class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/edit.html'
    success_url = reverse_lazy('main')
    form_class = ShopUserEditForm


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
