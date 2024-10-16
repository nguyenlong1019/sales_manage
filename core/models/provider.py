from django.db import models 
from inventory_system.utils import CommonAbstract 


class Provider(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã nhà cung cấp')
    name = models.CharField(max_length=50, verbose_name='Tên nhà cung cấp')
    legal_repr = models.CharField(max_length=50, null=True, blank=True, verbose_name='Người đại diện') # legal representative 
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Số điện thoại')
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Email')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Địa chỉ')
    acc_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Số tài khoản')
    tax_code = models.CharField(max_length=15, null=True, blank=True, verbose_name='Mã số thuế')
    status = models.BooleanField(default=False, verbose_name='Trạng thái hoạt động')


    class Meta:
        verbose_name = 'Nhà cung cấp'
        verbose_name_plural = 'Nhà cung cấp'
        db_table = 'provider'


    def __str__(self):
        return f"{self.id} - {self.name}"

