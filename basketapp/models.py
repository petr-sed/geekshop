from django.db import models
from django.conf import settings
from mainapp.models import Product

class Basket(models.Model):
    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user.username, self.product.name)

    def get_cost(self):
        return self.quantity * self.product.price

    cost = property(get_cost)