from django.db import models 
from inventory_system.utils import CommonAbstract 
from .product import Product 
from .unit import Unit 
from .price import Price 


class PriceDetail(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã chi tiết chào giá')
    price_code = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True, db_column='price_id', verbose_name='Mã chào giá')
    product = models.ForeignKey(Product, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Mã hàng')
    unit = models.ForeignKey(Unit, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Đơn vị tính')
    qty = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Số lượng')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Đơn giá')
    discount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Triết khấu (%)')
    tax = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Thuế (%)')
    cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Phí')

    class Meta:
        verbose_name = 'Chi tiết chào giá'
        verbose_name_plural = 'Chi tiết chào giá'
        db_table = 'price_detail'


    def __str__(self):
        return f"{self.id}"
