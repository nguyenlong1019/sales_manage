from django.db import models 
from inventory_system.utils import CommonAbstract
from .refund import Refund 
from .product import Product 
from .unit import Unit 


class RefundDetail(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    refund = models.ForeignKey(Refund, on_delete=models.SET_NULL, null=True, verbose_name='Mã trả hàng')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Mã hàng hóa')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, verbose_name='Đơn vị tính')
    quantity = models.IntegerField(default=1, verbose_name='Số lượng')
    price = models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Giá')
    discount = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, verbose_name='% Chiết khấu')
    tax = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, verbose_name='% Thuế')
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ghi chú')


    class Meta:
        verbose_name = 'Chi tiết trả hàng'
        verbose_name_plural = 'Chi tiết trả hàng'
        db_table = 'refund_detail'

    
    def __str__(self):
        return f"{self.id} - {self.quantity}"

