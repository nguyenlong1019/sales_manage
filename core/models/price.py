from django.db import models
from inventory_system.utils import CommonAbstract 
from .buy_require import BuyRequire
# from .order import Order 
from .provider import Provider 


class Price(CommonAbstract):
    PRICE_STATUS = (
        (0, 'draft'),
        (1, 'pending'),
        (2, 'accepted'),
        (3, 'rejected'),
    )

    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã chào giá')
    desc = models.CharField(max_length=255, verbose_name='Diễn giải')
    buy_require = models.ForeignKey(BuyRequire, on_delete=models.SET_NULL, null=True, verbose_name='Mã yêu cầu')
    provider = models.ForeignKey(Provider, to_field='id', on_delete=models.SET_NULL, null=True, verbose_name='Mã nhà cung cấp')
    price_date = models.DateField(verbose_name='Ngày chào giá')
    expire = models.IntegerField(default=1, verbose_name='Thời gian hiệu lực (ngày)')
    status = models.IntegerField(default=1, choices=PRICE_STATUS, verbose_name='Trạng thái chào giá') 

    class Meta:
        verbose_name = 'Chào giá'
        verbose_name_plural = 'Chào giá'
        db_table = 'price'


    def __str__(self):
        return f"{self.id} - {self.status}"
