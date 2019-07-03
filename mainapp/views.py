from django.shortcuts import render, get_object_or_404
import json
from .models import Product, ProductCategory
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

with open("db.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

links_sec_menu = ProductCategory.objects.all()
titles = data['titles']

def main(request):
    products = Product.objects.all()
    hot_product = Product.objects.filter(is_hot=True).order_by('?')
    hot_product = hot_product[:3]
    content = {
                'titles': titles,
                'products_4': products[:4],
                'products_6': products[4:10],
                'products_22': products[10:14],
                'hot_product_2': hot_product[:2],
                'hot_product_1': hot_product[2],
            }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None, page=1):
    """products filter"""
    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        """hot_product"""
        hot_product = Product.objects.filter(is_hot=True).order_by('?')
        hot_product = hot_product[:2]

        """paginator"""
        paginator = Paginator(products, 6)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
                   'links_sec_menu': links_sec_menu,
                   'products': products_paginator,
                   'titles': titles,
                   'hot_product': hot_product,
                   'category': category,
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
