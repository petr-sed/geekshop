from django.shortcuts import render
import json
from .models import Product, ProductCategory

# Create your views here.

with open("db.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

links_sec_menu = ProductCategory.objects.all()
product_2 = data['product_2']
titles = data['titles']

def main(request):
    products = Product.objects.all()
    content = {
                'titles': titles,
                'products_4': products[:4],
                'products_6': products[4:10],
                'products_22': products[10:],
                'product_2': product_2
              }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    if pk is not None:
        products = Product.objects.filter(category_id=pk)
        media = '../../media/'
    else:
        products = Product.objects.all()[:12]
        media = '../media/'
    content = {
               'links_sec_menu': links_sec_menu,
               'products_12': products,
               'titles': titles,
               'product_2': product_2,
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
    content = {
                'links_sec_menu': links_sec_menu,
                'titles': titles,
                'product_2': product_2,
                'product' : product,
                'products': products,
              }
    return render(request, 'mainapp/deal.html', content)
