from django.contrib import admin
from core.models.product_type import ProductType 
from core.models.product import Product 
from core.models.unit import Unit 
from core.models.order import Order 
from core.models.order_detail import OrderDetail
from core.models.provider import Provider 
from core.models.price import Price 
from core.models.price_detail import PriceDetail


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


