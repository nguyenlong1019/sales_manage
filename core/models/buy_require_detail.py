from django.db import models 
from inventory_system.utils import CommonAbstract 
from .product import Product 
from .unit import Unit 


class BuyRequireDetail(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã yêu cầu mua')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Mã hàng')
    unit = models.ForeignObjectRel(Unit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Đơn vị tính')
    quantity = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Số lượng')


    class Meta:
        verbose_name = 'Chi tiết yêu cầu mua'
        verbose_name_plural = 'Chi tiết yêu cầu mua'
        db_table = 'buy_require_detail'


    def __str__(self):
        return f"{self.id} - {self.quantity}"