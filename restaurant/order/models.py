from django.db import models
from account.models import Profile
from menu.models import MenuItems, Toppings
from decimal import *

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False, blank=True, null=True)
    transanction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.get_total
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.quantity
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(MenuItems, on_delete=models.SET_NULL, blank=True, null=True)
    topping_1 = models.CharField(max_length=200, null=True, blank=True)
    topping_2 = models.CharField(max_length=200, null=True, blank=True)
    topping_3 = models.CharField(max_length=200, null=True, blank=True)
    topping_4 = models.CharField(max_length=200, null=True, blank=True)
    topping_5 = models.CharField(max_length=200, null=True, blank=True)
    extra_cheese = models.BooleanField(default=False, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.item_name

    @property
    def get_total(self):
        if self.extra_cheese == True:
            price = self.product.item_price + Decimal(0.50)
            total = price * self.quantity
        else:
            total = self.product.item_price * self.quantity
        return total

        




class DeliveryAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address