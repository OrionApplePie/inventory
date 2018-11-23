# coding: utf-8
from django.db import models

class Inventory(models.Model):
    """Модель инвентаря - компьютер или сервер."""
    INV_TYPES = (
        (0, 'Сервер'),
        (1, 'Простой АРМ'),
        (2, 'Ноутбук')
    )
    title = models.CharField(max_length=50)

    inventory_type = models.IntegerField(
        max_length = 24,
        choices=INV_TYPES
    )
    
    inventory_number = models.CharField(max_length=16)
    
    def __str__(self):
        return "%s " % (self.title)


class Software(models.Model):
    """Модель для ПО."""
    title = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    
    serial = models.CharField(max_length=50)

    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE
    )
    
    def __str__(self):
        return "%s " % (self.title)
