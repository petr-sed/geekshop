from django.contrib import admin
from .models import ProductCategory, Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'category', 'is_hot', 'is_active',
    list_filter = 'is_hot', 'is_active',
    search_fields = 'name', 'category__name', 'short_desc', 'description',
    readonly_fields = 'quantity',

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'is_active',
    list_filter = 'is_active',
    search_fields = 'name', 'description',
