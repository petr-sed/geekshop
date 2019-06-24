from django.shortcuts import render, get_object_or_404
import json
from .models import Product, ProductCategory
from basketapp.models import Basket


# Create your views here.

with open("db.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

links_sec_menu = ProductCategory.objects.all()
titles = data['titles']

def main(request):
    products = Product.objects.all()
    hot_product = []
    hot_product.append(Product.objects.filter(is_hot=True).order_by('?').first())
    hot_product.append(Product.objects.filter(is_hot=True).order_by('?').first())
    content = {
                'titles': titles,
                'products_4': products[:4],
                'products_6': products[4:10],
                'products_22': products[10:14],
                'hot_product': hot_product,
            }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category)
        media = '../../media/'
    else:
        products = Product.objects.all()[:12]
        media = '../media/'
    hot_product = []
    hot_product.append(Product.objects.filter(is_hot=True).order_by('?').first())
    hot_product.append(Product.objects.filter(is_hot=True).order_by('?').first())
    content = {
               'links_sec_menu': links_sec_menu,
               'products_12': products,
               'titles': titles,
               'hot_product': hot_product,
               'media': media,
               }
    return render(request, 'mainapp/catalog.html', content)

def contact(request):
    content = {
                'titles': titles
              }
    return render(request, 'mainapp/contacts.html', content)

def deal(request, pk=None):
    product = Product.objects.filter(id=pk).first()
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
                'links_sec_menu': links_sec_menu,
                'titles': titles,
                'product': product,
                'products': products,
                'basket': basket
              }
    return render(request, 'mainapp/deal.html', content)
