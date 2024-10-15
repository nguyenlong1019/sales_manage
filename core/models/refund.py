from django.db import models 
from inventory_system.utils import CommonAbstract 
from .order import Order


class Refund(CommonAbstract):
    STATUS = (
        (0, 'Draft'),
        (1, 'Waiting'),
        (2, 'Pending'),
        (3, 'Refunded')
    )

    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã trả hàng')
    reason = models.CharField(max_length=255, verbose_name='Lý do')
    refund_date = models.DateField(verbose_name='Ngày trả')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Mã đơn hàng')
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ghi chú')
    status = models.IntegerField(default=0, verbose_name='Trạng thái trả hàng', choices=STATUS)


    class Meta:
        verbose_name = 'Trả hàng'
        verbose_name_plural = 'Trả hàng'
        db_table = 'refund'

    
    def __str__(self):
        return f"{self.id} - {self.reason}"
