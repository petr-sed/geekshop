from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
import json, os
from geekshop.settings import config, local_config_path

config.read(local_config_path)

JSON_PATH = 'mainapp/json'

def LoadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name+'.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = LoadFromJSON('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = LoadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = ProductCategory.objects.get(name=category_name)
            product["category"] = _category
            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.all().delete()
        ShopUser.objects.create_superuser(config.get('admin', 'SUPER_USER'))


