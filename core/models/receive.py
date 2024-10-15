from django.db import models 
from inventory_system.utils import CommonAbstract 
from .provider import Provider 
from .order import Order 


class Receive(CommonAbstract):
    STATUS = (
        (0, 'Draft'),
        (0, 'Pending'),
        (0, 'Done'),
    )

    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã nhận hàng')
    description = models.TextField(verbose_name='Diễn giải')
    receive_date = models.DateField(verbose_name='Ngày nhận')
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, verbose_name='Nhà cung cấp')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Mã đơn hàng')
    sender = models.CharField(max_length=50, verbose_name='Người giao')
    receiver = models.CharField(max_length=50, verbose_name='Người nhận')
    status = models.IntegerField(default=0, verbose_name='Trạng thái thanh toán')


    class Meta:
        verbose_name = 'Nhận hàng'
        verbose_name_plural = 'Nhận hàng'
        db_table = 'receive'
