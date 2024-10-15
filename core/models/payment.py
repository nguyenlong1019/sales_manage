from django.db import models 
from inventory_system.utils import CommonAbstract
from .order import Order 
from .payment_schedule import PaymentSchedule 


class Payment(CommonAbstract):
    PAYMENT_STATUS = (
        (0, 'Draft'),
        (1, 'Waiting'),
        (2, 'Pending'),
        (3, 'Done'),
    )

    id = models.CharField(max_length=15, primary_key=True, verbose_name='Mã thanh toán')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Mã đơn hàng')
    times = models.ForeignKey(PaymentSchedule, on_delete=models.SET_NULL, null=True, to_field='times', verbose_name='Số lần thanh toán')
    payment_date = models.DateField(verbose_name='Ngày thanh toán')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Mô tả')
    amount = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Số tiền')
    status = models.IntegerField(default=0, verbose_name='Trạng thái thanh toán', choices=PAYMENT_STATUS)


    class Meta:
        verbose_name = 'Thanh toán'
        verbose_name_plural = 'Thanh toán'
        db_table = 'payment'

    
    def __str__(self):
        return f"{self.id} - {self.amount}"
