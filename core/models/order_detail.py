from django.db import models
from inventory_system.utils import CommonAbstract
from .product import Product 
from .unit import Unit
from .order import Order 


class OrderDetail(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã chi tiết đơn mua')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Mã đơn mua')
    product = models.ForeignKey(Product, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Mã hàng')
    unit = models.ForeignKey(Unit, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Đơn vị tính')
    qty = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Số lượng')
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Đơn giá')
    discount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, verbose_name='Chiết khấu (%)')
    tax = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, verbose_name='Thuế (%)')
    cost = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, verbose_name='Phí')


    class Meta:
        verbose_name = 'Chi tiết đơn mua'
        verbose_name_plural = 'Chi tiết đơn mua'
        db_table = 'order_detail'

    
    def __str__(self):
        return f"{self.id}"

