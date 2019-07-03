from django import template
from basketapp.models import Basket
from django.conf import settings
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

@register.filter(name='media_folder_products')
def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'products_images/default.jpg'

    return '{}{}'.format(settings.MEDIA_URL, string)


@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not string:
        string = 'users_avatars/default.jpg'

    return '{}{}'.format(settings.MEDIA_URL, string)
