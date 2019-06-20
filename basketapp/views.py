from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from django.urls import reverse


def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        total_price = {}
        for object in basket:
            total_price[object.product.name] = object.product.price * object.quantity
        final_price = sum(total_price.values())
        content = {
            'final_price': final_price,
            'total_price': total_price,
            'basket': basket,
        }
        return render(request, 'basketapp/basket.html', content)
    else:
        return HttpResponseRedirect(reverse('main'))

def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)
