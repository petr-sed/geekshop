from django.shortcuts import render

# Create your views here.

links_menu = [
    {'href': 'main', 'name': 'HOME'},
    {'href': 'products', 'name': 'PRODUCTS'},
    {'href': 'main', 'name': 'HISTORY'},
    {'href': 'main', 'name': 'SHOWROOM'},
    {'href': 'contact', 'name': 'CONTACT'},
]

links_sec_menu = [
    {'href': 'products', 'name': 'все'},
    {'href': 'products', 'name': 'дом'},
    {'href': 'products', 'name': 'офис'},
    {'href': 'products', 'name': 'модерн'},
    {'href': 'products', 'name': 'классика'},
]

def main(request):
    content = {'links_menu': links_menu, 'title': 'title'}
    return render(request, 'mainapp/index.html', content)

def products(request):
    content = {'links_menu': links_menu, 'links_sec_menu': links_sec_menu, 'title': 'title'}
    return render(request, 'mainapp/catalog.html', content)

def contact(request):
    content = {'links_menu': links_menu, 'title': 'title'}
    return render(request, 'mainapp/contacts.html', content)

def deal(request):
    content = {'links_menu': links_menu, 'links_sec_menu': links_sec_menu, 'title': 'title'}
    return render(request, 'mainapp/deals.html', content)
