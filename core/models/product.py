from django.db import models 
from inventory_system.utils import CommonAbstract 
from .product_type import ProductType 
from .unit import Unit


class Product(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True)
    type = models.ForeignKey(ProductType, to_field='id', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, to_field='id', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Hàng hóa'
        verbose_name_plural = 'Hàng hóa'
        db_table = 'products'


    def __str__(self):
        return f"{self.id} - {self.name}"

