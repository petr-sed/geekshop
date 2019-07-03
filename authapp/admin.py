from django.contrib import admin
from .models import ShopUser
from basketapp.models import Basket

class BasketInline(admin.TabularInline):
    model = Basket
    field = 'product', 'quantity'
    extra = 1

@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    list_display = 'username', 'is_superuser','is_active',
    list_filter = 'is_superuser','is_active',
    search_fields = 'username', 'last_name', 'first_name', 'email',
    readonly_fields = 'password',

class UserWithBasketAdmin(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True

@admin.register(UserWithBasketAdmin)
class ShopUserWithBasketAdmin(admin.ModelAdmin):
    fields = 'username',
    list_display = 'username', 'is_superuser','is_active', 'get_basket_quantity', 'get_basket_cost',
    list_filter = 'is_superuser','is_active',
    search_fields = 'username', 'last_name', 'first_name', 'email',
    readonly_fields = 'username',
    inlines = BasketInline,

    def get_queryset(self, request):
        qs = super(ShopUserWithBasketAdmin, self).get_queryset(request)
        return qs.filter(basket__quantity__gt = 0).distinct()

    def get_basket_quantity(self, instance):
        basket = Basket.objects.filter(user = instance)
        return sum(list(map(lambda basket: basket.quantity, basket)))

    get_basket_quantity.short_description = 'Товаров в корзине'

    def get_basket_cost(self, instance):
        basket = Basket.objects.filter(user = instance)
        return sum(list(map(lambda basket: basket.cost, basket)))

    get_basket_cost.short_description = 'Общая стоимость'