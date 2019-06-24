from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        content = {
            'basket': basket,
        }
        return render(request, 'basketapp/basket.html', content)
    else:
        return HttpResponseRedirect(reverse('main'))

@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('deal', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if basket:
        if basket.quantity == 1:
            basket.delete()
            basket.save()
        else:
            basket.quantity -= 1
            basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
