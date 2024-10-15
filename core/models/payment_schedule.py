from django.db import models 
from inventory_system.utils import CommonAbstract


class PaymentSchedule(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True, verbose_name='')
    start_date = models.DateField(verbose_name='')
    end_date = models.DateField(verbose_name='')
    times = models.IntegerField(default=1, verbose_name='')
    amount = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='')


    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        db_table = 'payment_schedule'


    def __str__(self):
        return f"{self.id} - {self.amount}"    
    