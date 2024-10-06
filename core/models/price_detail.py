from django.db import models 
from inventory_system.utils import CommonAbstract 
from .product import Product 
from .unit import Unit 


class PriceDetail(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, to_field='id', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=12, decimal_places=2)
    tax = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Chi tiết chào giá'
        verbose_name_plural = 'Chi tiết chào giá'
        db_table = 'price_detail'
