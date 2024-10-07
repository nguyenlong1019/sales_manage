from django.db import models 
from inventory_system.utils import CommonAbstract


class PaymentSchedule(CommonAbstract):
    id = models.CharField(max_length=15, primary_key=True)
    