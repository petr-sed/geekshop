from django.shortcuts import render
import json

# Create your views here.

with open("db.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

links_menu = data['links_menu']
links_sec_menu = data['links_sec_menu']
product_2 = data['product_2']

def main(request):
    content = {'links_menu': links_menu, 'title': 'title', 'product_2': product_2}
    return render(request, 'mainapp/index.html', content)

def products(request):
    content = {'links_menu': links_menu, 'links_sec_menu': links_sec_menu, 'title': 'title', 'product_2': product_2}
    return render(request, 'mainapp/catalog.html', content)

def contact(request):
    content = {'links_menu': links_menu, 'title': 'title'}
    return render(request, 'mainapp/contacts.html', content)

def deal(request):
    content = {'links_menu': links_menu, 'links_sec_menu': links_sec_menu, 'title': 'title', 'product_2': product_2}
    return render(request, 'mainapp/deals.html', content)
