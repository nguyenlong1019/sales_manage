from django.db import models 
from inventory_system.utils import CommonAbstract 
from .price import Price 
from .provider import Provider 


class Order(CommonAbstract):
    ORDER_STATUS = (
        (0, 'Draft'),
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Canceled'),
    )

    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã đơn mua')
    desc = models.CharField(max_length=50, verbose_name='Diễn giải')
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True, verbose_name='Mã chào giá')
    order_date = models.DateField(verbose_name='Ngày hóa đơn')
    deli_date = models.DateField(null=True, verbose_name='Ngày giao hàng')
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, verbose_name='Nhà cung cấp')
    status = models.IntegerField(default=1, choices=ORDER_STATUS, verbose_name='Trạng thái đơn hàng')

    class Meta:
        verbose_name = 'Đơn mua'
        verbose_name_plural = 'Đơn mua'
        db_table = 'orders'


    def __str__(self):
        return f"{self.id}"
    