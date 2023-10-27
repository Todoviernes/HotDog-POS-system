from django.db import models

from pos.users.models import User

# Create your models here.


class HotDogStand(models.Model):
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class InventoryItem(models.Model):
    name = models.CharField(max_length=255)


class Inventory(models.Model):
    hotdog_stand = models.ForeignKey(HotDogStand, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    threshold = models.PositiveIntegerField()

    def is_below_threshold(self):
        return self.quantity < self.threshold


class Sale(models.Model):
    hotdog_stand = models.ForeignKey(HotDogStand, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
