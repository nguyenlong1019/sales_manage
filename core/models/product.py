from django.db import models 
from inventory_system.utils import CommonAbstract 
from .product_type import ProductType 
from .unit import Unit


class Product(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã hàng hóa')
    type = models.ForeignKey(ProductType, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Loại hàng hóa')
    name = models.CharField(max_length=50, verbose_name='Tên hàng hóa')
    unit = models.ForeignKey(Unit, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Đơn vị tính')


    class Meta:
        verbose_name = 'Hàng hóa'
        verbose_name_plural = 'Hàng hóa'
        db_table = 'products'


    def __str__(self):
        return f"{self.id} - {self.name}"

