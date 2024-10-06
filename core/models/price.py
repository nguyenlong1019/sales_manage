from django.db import models
from inventory_system.utils import CommonAbstract 
from .order import Order 
from .provider import Provider 


class Price(CommonAbstract):
    PRICE_STATUS = (
        (0, 'draft'),
        (1, 'pending'),
        (2, 'accepted'),
        (3, 'rejected'),
    )

    id = models.CharField(max_length=15, primary_key=True)
    desc = models.CharField(max_length=255)
    order = models.ForeignKey(Order, to_field='id', on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, to_field='provider_id', on_delete=models.CASCADE)
    price_date = models.DateField(null=False)
    expire = models.IntegerField(default=1)
    status = models.IntegerField(default=1, choices=PRICE_STATUS) 

    class Meta:
        verbose_name = 'Chào giá'
        verbose_name_plural = 'Chào giá'
        db_table = 'price'

