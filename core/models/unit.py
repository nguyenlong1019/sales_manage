from django.db import models 
from inventory_system.utils import CommonAbstract 


class Unit(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã đơn vị')
    desc = models.CharField(max_length=50, verbose_name='Mô tả')


    class Meta:
        verbose_name = 'Đơn vị hàng hóa'
        verbose_name_plural = 'Đơn vị hàng hóa'
        db_table = 'units'


    def __str__(self):
        return f"{self.id} - {self.desc}"

