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

from django.http import HttpResponse 
from django import forms 


# Action: Lập báo cáo mua hàng 
def report_purchased_items(modeladmin, request, queryset):
    # Báo cáo các mặt hàng đã mua 
    purchased_items = queryset.filter(status='purchased') # lọc theo trạng thái đã mua 
    report = "Báo cáo các hàng đã mua\n\n"

    for order in purchased_items:
        report += f"Đơn hàng ID: {order.id}, Khách hàng: {order.customer_name}, Số lượng: {order.quantity}, Ngày mua: {order.purchase_date}\n"
    
    response = HttpResponse(report, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=purchased_items_report.txt'
    return response 


# Action: Báo cáo các đơn hàng chưa thanh toán 
def report_unpaid_orders(modeladmin, request, queryset):
    # Tạo một báo cáo cho các đơn hàng chưa thanh toán 
    unpaid_orders = queryset.filter(status='unpaid') # Lọc theo trạng thái chưa thanh toán 
    report = "Báo cáo các đơn hàng chưa thanh toán\n\n"

    for order in unpaid_orders:
        report += f"Đơn hàng ID: {order.id}, Khách hàng: {order.customer_name}, Tổng tiền: {order.total_amount}, Hạn thanh toán: {order.due_date}\n" 

    response = HttpResponse(report, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=unpaid_orders_report.txt'
    return response


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'legal_repr', 'phone', 'email', 'address', 'acc_number', 'tax_code', 'status']
    list_display = ['id', 'name', 'legal_repr', 'phone', 'email', 'address', 'acc_number', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    readonly_fields = ['created_at',]
    # list_display = [] # các trường hiển thị
    # list_display_links = [] # link đến trang chi tiết chỉnh sửa
    # list_editable = [] # danh sách các trường có thể chỉnh sửa 
    # list_max_show_all = [] # số object tối đa trên một trang 
    # list_per_page = [] # số object trên mỗi trang 
    # list_select_related = [] # object related trong foreignkey


class ProductInline(admin.TabularInline):
    model = Product 
    extra = 1


# @admin.register(ProductType)
# class ProductTypeAdmin(admin.ModelAdmin):
#     search_fields = ['id', 'name']
#     readonly_fields = ['created_at',]
#     # inlines = [ProductInline]


# @admin.register(Unit)
# class UnitAdmin(admin.ModelAdmin):
#     search_fields = ['id', ]
#     readonly_fields = ['created_at',]


class HiddenModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False 
    
admin.site.register(ProductType, HiddenModelAdmin)
admin.site.register(Unit, HiddenModelAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    readonly_fields = ['created_at', ]
    list_display = ['id', 'name']
    # list_display = ('id', 'name', 'type', 'unit')  # Hiển thị trong danh sách admin
    # autocomplete_fields = ['type', 'unit']  # Sử dụng autocomplete cho khóa ngoại


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail 
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['id', ] 
    readonly_fields = ['created_at', ]
    list_display = ['id', 'price', 'order_date', 'deli_date', 'provider', 'status']
    inlines = [OrderDetailInline] 
    actions = [report_purchased_items, report_unpaid_orders]


# @admin.register(OrderDetail)
# class OrderDetail(admin.ModelAdmin):
#     search_fields = ['id', ]
#     readonly_fields = ['created_at', ]


class PriceDetailInline(admin.TabularInline):
    model = PriceDetail 
    extra = 3


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 
    list_display = ['id', 'buy_require', 'provider', 'price_date', 'expire', 'status', 'created_at', 'updated_at']
    inlines = [PriceDetailInline]


# @admin.register(PriceDetail)
# class PriceDetailAdmin(admin.ModelAdmin):
#     search_fields = ['id', ]
#     readonly_fields = ['created_at', ] 


class BuyRequireDetailInline(admin.TabularInline):
    model = BuyRequireDetail 
    extra = 4 


@admin.register(BuyRequire)
class BuyRequireAdmin(admin.ModelAdmin):
    search_fields = ['id', ] 
    readonly_fields = ['created_at', ] 
    inlines = [BuyRequireDetailInline] 
    list_display = ['id', 'created_date', 'expired_date', 'created_by', 'status', 'created_at', 'updated_at']


# @admin.register(BuyRequireDetail)
# class BuyRequireDetailAdmin(admin.ModelAdmin):
#     search_fields = ['id', ]
#     readonly_fields = ['created_at', ] 


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 
    list_display = ['id', 'order', 'times', 'payment_date', 'description', 'amount', 'status', 'created_at', 'updated_at']


@admin.register(PaymentSchedule)
class PaymentScheduleAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 
    list_display = ['id', 'order', 'start_date', 'end_date', 'times', 'amount', 'created_at', 'updated_at']


class ReceiveDetailInline(admin.TabularInline):
    model = ReceiveDetail 
    extra = 3


@admin.register(Receive)
class ReceiveAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 
    inlines = [ReceiveDetailInline]
    list_display = ['id', 'receive_date', 'provider', 'order', 'sender', 'receiver', 'status', 'created_at', 'updated_at']


# @admin.register(ReceiveDetail)
# class ReceiveDetailAdmin(admin.ModelAdmin):
#     search_fields = ['id', ] 
#     readonly_fields = ['created_at', ] 


class RefundDetailInline(admin.TabularInline):
    model = RefundDetail 
    extra = 3 


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    readonly_fields = ['created_at', ] 
    inlines = [RefundDetailInline] 
    list_display = ['id', 'refund_date', 'order', 'status', 'created_at', 'updated_at']


# @admin.register(RefundDetail)
# class RefundDetailAdmin(admin.ModelAdmin):
#     search_fields = ['id', ]
#     readonly_fields = ['created_at', ] 
