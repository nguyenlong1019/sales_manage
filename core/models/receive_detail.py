from django.db import models 
from inventory_system.utils import CommonAbstract 
from .receive import Receive 
from .product import Product 
from .unit import Unit 


class ReceiveDetail(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    receive = models.ForeignKey(Receive, on_delete=models.SET_NULL, null=True, verbose_name='Mã nhận hàng')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Mã hàng hóa')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, verbose_name='Đơn vị tính')
    quantity = models.IntegerField(default=1, verbose_name='Số lượng')
    price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Giá')
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='% Chiết khấu')
    tax = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='% Thuế')
    cost = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True, verbose_name='Phí')


    class Meta:
        verbose_name = 'Chi tiết nhận hàng'
        verbose_name_plural = 'Chi tiết nhận hàng'
        db_table = 'receive_detail'

    def __str__(self):
        return f"{self.id} - {self.quantity}"
