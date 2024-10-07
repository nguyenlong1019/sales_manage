from django.db import models
from inventory_system.utils import CommonAbstract


class BuyRequire(CommonAbstract):
    STATUS = (
        (0, 'draft'),
        (1, 'pending'),
        (2, 'accepted'),
        (3, 'rejected'),
    )

    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã yêu cầu')
    desc = models.CharField(max_length=50, verbose_name='Mô tả')
    created_date = models.DateField(verbose_name='Ngày yêu cầu')
    expired_date = models.DateField(null=True, blank=True, verbose_name='Ngày cần')
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ghi chú')
    created_by = models.CharField(max_length=50, null=True, blank=True, verbose_name='Người yêu cầu')
    status = models.SmallIntegerField(default=0, choices=STATUS, verbose_name='Trạng thái yêu cầu')


    class Meta:
        verbose_name = 'Yêu cầu mua'
        verbose_name_plural = 'Yêu cầu mua'
        db_table = 'buy_required'

    
    def __str__(self):
        return f"{self.id} - {self.status}"
    

