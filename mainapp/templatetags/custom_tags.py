from django import template
register = template.Library()

@register.filter
def basket_total_quantity(user):
    if user.is_anonymus:
        return 0
    else:
        basket = user.basket.all()
        total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
        return total_quantity

@register.filter
def bascet_total_cost(user):
    if user.is_anonymus:
        return 0
    else:
        basket = user.basket.all()
        total_cost = sum(list(map(lambda basket_slot: basket_slot.cost, basket)))
        return total_cost