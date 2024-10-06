from django.db import models 
from inventory_system.utils import CommonAbstract 
from django.contrib.auth.models import User 


class Order(CommonAbstract):
    ORDER_STATUS = (
        (0, 'Draft'),
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    )

    id = models.CharField(max_length=15, primary_key=True)
    desc = models.CharField(max_length=50)
    order_date = models.DateField(null=False)
    deli_date = models.DateField(null=False)
    note = models.CharField(max_length=255, null=True, blank=True)
    person_name = models.CharField(max_length=50, null=True, blank=True)
    status = models.IntegerField(default=1, choices=ORDER_STATUS)

    class Meta:
        verbose_name = 'Đơn mua'
        verbose_name_plural = 'Đơn mua'
        db_table = 'orders'