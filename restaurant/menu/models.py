from django.db import models

class Toppings(models.Model):
    item_name = models.CharField(max_length=64)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.item_name

class MenuItems(models.Model):
    item_type = models.CharField(max_length=32)
    item_name = models.CharField(max_length=64)
    item_size = models.CharField(max_length=64, blank=True,null=True)
    no_topping = models.IntegerField(default=0, blank=True, null=True)
    toppings_1 = models.ForeignKey(Toppings, related_name="topping_1", on_delete=models.SET_NULL, blank=True, null=True)
    toppings_2 = models.ForeignKey(Toppings, related_name="topping_2", on_delete=models.SET_NULL, blank=True, null=True)
    toppings_3 = models.ForeignKey(Toppings, related_name="topping_3", on_delete=models.SET_NULL, blank=True, null=True)
    toppings_4 = models.ForeignKey(Toppings, related_name="topping_4", on_delete=models.SET_NULL, blank=True, null=True)
    toppings_5 = models.ForeignKey(Toppings, related_name="topping_5", on_delete=models.SET_NULL, blank=True, null=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    item_image = models.ImageField(null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item_type

    @property
    def imageURL(self):
        try:
            url = self.item_image.url
        except:
            url = ''
        return url