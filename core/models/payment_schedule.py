from django.db import models 
from inventory_system.utils import CommonAbstract 
from .order import Order 


class PaymentSchedule(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Mã đơn mua')
    start_date = models.DateField(verbose_name='Ngày bắt đầu thanh toán')
    end_date = models.DateField(verbose_name='Ngày kết thúc thanh toán')
    times = models.IntegerField(default=1, verbose_name='Số lần thanh toán', unique=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Số tiền')


    class Meta:
        verbose_name = 'Lịch thanh toán'
        verbose_name_plural = 'Lịch thanh toán'
        db_table = 'payment_schedule'


    def __str__(self):
        return f"{self.id} - {self.amount}"    
    