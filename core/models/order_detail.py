from django.db import models
from inventory_system.utils import CommonAbstract
from .product import Product 
from .unit import Unit


class OrderDetail(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, to_field='id', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)


    class Meta:
        verbose_name = 'Chi tiết đơn mua'
        verbose_name_plural = 'Chi tiết đơn mua'
        db_table = 'order_detail'

