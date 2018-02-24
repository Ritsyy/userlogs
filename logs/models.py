from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from simple_history import register
from simple_history.models import HistoricalRecords


register(User, inherit=True)


class Variant(models.Model):

    SIZE_CHOICES = (
        (None, ('Please Select')),
        ('S', ('SMALL')),
        ('M', ('MEDIUM')),
        ('L', ('LARGE')),
        ('XL', ('EXTRA LARGE')),
    )

    size = models.CharField(choices=SIZE_CHOICES, max_length=3, default=None, blank=True, null=True)
    cloth = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50)
    selling_price = models.IntegerField()
    cost_price = models.IntegerField()
    quantity = models.IntegerField()
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    history = HistoricalRecords(inherit=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, null=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    product_code = models.TextField()

    def __str__(self):
        return self.name
