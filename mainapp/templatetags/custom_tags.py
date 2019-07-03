from django import template
from basketapp.models import Basket
register = template.Library()

@register.filter
def basket_total_quantity(user):
    if user.is_anonymous:
        return 0
    else:
        basket = user.basket.all()
        total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
        return total_quantity

@register.filter
def basket_total_cost(user):
    if user.is_anonymous:
        return 0
    else:
        basket = Basket.objects.select_related('product').filter(user=user)
        total_cost = sum(list(map(lambda basket_slot: basket_slot.cost, basket)))
        return total_cost