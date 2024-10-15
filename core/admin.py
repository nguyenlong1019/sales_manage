from django.contrib import admin
from core.models.product_type import ProductType 
from core.models.product import Product 
from core.models.unit import Unit 
from core.models.order import Order 
from core.models.order_detail import OrderDetail
from core.models.provider import Provider 
from core.models.price import Price 
from core.models.price_detail import PriceDetail 
from core.models.buy_require import BuyRequire
from core.models.buy_require_detail import BuyRequireDetail 
from core.models.payment import Payment 
from core.models.payment_schedule import PaymentSchedule 
from core.models.receive import Receive 
from core.models.receive_detail import ReceiveDetail 
from core.models.refund import Refund 
from core.models.refund_detail import RefundDetail


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    search_fields = ['provider_id',]
    readonly_fields = ['created_at',]


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    readonly_fields = ['created_at',]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['id', ] 
    readonly_fields = ['created_at', ]


@admin.register(OrderDetail)
class OrderDetail(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(PriceDetail)
class PriceDetailAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(BuyRequire)
class BuyRequireAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(BuyRequireDetail)
class BuyRequireDetailAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(PaymentSchedule)
class PaymentScheduleAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(Receive)
class ReceiveAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(ReceiveDetail)
class ReceiveDetailAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 


@admin.register(RefundDetail)
class RefundDetailAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 
