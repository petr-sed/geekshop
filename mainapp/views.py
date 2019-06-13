from django.shortcuts import render
import json
from .models import Product, ProductCategory

# Create your views here.

with open("db.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

links_menu = data['links_menu']
links_sec_menu = data['links_sec_menu']
product_2 = data['product_2']
titles = data['titles']

def main(request):
    products = Product.objects.all()
    content = {
                'links_menu': links_menu,
                'titles': titles,
                'products_4': products[:4],
                'products_6': products[4:10],
                'products_22': products[10:],
                'product_2': product_2
              }
    return render(request, 'mainapp/index.html', content)

def products(request):
    products = Product.objects.all()
    content = {
               'links_menu': links_menu,
               'links_sec_menu': links_sec_menu,
               'products_12': products[:12],
               'titles': titles,
               'product_2': product_2
               }
    return render(request, 'mainapp/catalog.html', content)

def contact(request):
    content = {
                'links_menu': links_menu,
                'titles': titles
              }
    return render(request, 'mainapp/contacts.html', content)

def deal(request):
    content = {
                'links_menu': links_menu,
                'links_sec_menu': links_sec_menu,
                'titles': titles,
                'product_2': product_2
              }
    return render(request, 'mainapp/deals.html', content)
