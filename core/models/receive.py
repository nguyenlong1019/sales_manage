from django.db import models 
from inventory_system.utils import CommonAbstract 
from .provider import Provider 
from .order import Order 


class Receive(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='')
    description = models.TextField()
    receive_date = models.DateField(verbose_name='')
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    sender = models.CharField(max_length=50, verbose_name='')
    receiver = models.CharField(max_length=50, verbose_name='')
    status = models.IntegerField(default=0)

