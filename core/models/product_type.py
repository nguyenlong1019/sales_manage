from django.db import models
from inventory_system.utils import CommonAbstract


class ProductType(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Loại hàng'
        verbose_name_plural = 'Loại hàng'
        db_table = 'product_type'

    
    def __str__(self):
        return f"{self.id} - {self.name}"
