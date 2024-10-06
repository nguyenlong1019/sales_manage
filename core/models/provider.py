from django.db import models 
from inventory_system.utils import CommonAbstract 


class Provider(CommonAbstract):
    provider_id = models.CharField(max_length=15, primary_key=True)
    provider_name = models.CharField(max_length=50)
    person = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    acc_number = models.CharField(max_length=50, null=True, blank=True)
    tax_code = models.CharField(max_length=15, null=True, blank=True)
    status = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Nhà cung cấp'
        verbose_name_plural = 'Nhà cung cấp'
        db_table = 'provider'


    def __str__(self):
        return f"{self.provider_id} - {self.provider_name}"

