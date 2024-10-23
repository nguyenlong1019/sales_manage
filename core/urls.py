from django.urls import path 
from core.views.index import * 

from core.views.manager.dashboard import * 
from core.views.manager.buy_require import * 
from core.views.manager.price import * 
from core.views.manager.order import * 
from core.views.manager.shipping import * 
from core.views.manager.payment import * 
from core.views.manager.report import * 

from core.views.staff.dashboard import * 
from core.views.staff.buy_require import * 
from core.views.staff.price import * 
from core.views.staff.order import * 
from core.views.staff.shipping import * 
from core.views.staff.report import * 


urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_view, name='logout'),

    path('manager/', manager_dashboard_view, name='manager-dashboard'),
    path('manager/login', login_manager_view, name='manager-login'),
    path('manager/buy-require', manager_buy_require_view, name='manager-buy-require'),
    path('manager/buy-require/add', manager_add_buy_require_view, name='manager-add-buy-require'),
    path('manager/buy-require/edit/<pk:pk>', manager_edit_buy_require_view, name='manager-edit-buy-require'),
    path('manager/buy-require/delete/<pk:pk>', manager_del_buy_require_view, name='manager-del-buy-require'),
    path('manager/price', manager_price_view, name='manager-price'),
    path('manager/price/add', manager_add_price_view, name='manager-add-price'),
    path('manager/price/edit/<pk:pk>', manager_edit_price_view, name='manager-edit-price'),
    path('manager/price/delete/<pk:pk>', manager_del_price_view, name='manager-del-price'),
    path('manager/order', manager_order_view, name='manager-order'),
    path('manager/order/add', manager_add_order_view, name='manager-add-order'),
    path('manager/order/edit/<pk:pk>', manager_edit_order_view, name='manager-edit-order'),
    path('manager/order/delete/<pk:pk>', manager_del_order_view, name='manager-del-order'),
    path('manager/shipping', manager_shipping_view, name='manager-shipping'),
    path('manager/shipping/add', manager_add_shipping_view, name='manager-add-shipping'),
    path('manager/shipping/edit/<pk:pk>', manager_edit_shipping_view, name='manager-edit-shipping'),
    path('manager/shipping/delete/<pk:pk>', manager_del_shipping_view, name='manager-del-shipping'),
    path('manager/payment', manager_payment_view, name='manager-payment'),
    path('manager/payment/edit/<pk:pk>', manager_payment_edit_view, name='manager-edit-payment'),
    path('manager/report', manager_report_view, name='manager-report'),
    path('manager/report/<pk:pk>', manager_edit_report_view, name='manager-edit-report'),

    path('staff/', staff_dashboard_view, name='staff-dashboard'),
    path('staff/login', login_staff_view, name='staff-login'),
    path('staff/buy-require', staff_buy_require_view, name='staff-buy-require'),    
    path('staff/buy-require/add', staff_add_buy_require_view, name='staff-add-buy-require'),    
    path('staff/buy-require/edit/<pk:pk>', staff_edit_buy_require_view, name='staff-edit-buy-require'),    
    path('staff/buy-require/delete/<pk:pk>', staff_del_buy_require_view, name='staff-del-buy-require'),
    path('staff/price'),    
    path('staff/price/add'),    
    path('staff/price/edit/<pk:pk>'),    
    path('staff/price/delete/<pk:pk>'),
    path('staff/order'),    
    path('staff/order/add'),    
    path('staff/order/edit/<pk:pk>'),    
    path('staff/order/delete/<pk:pk>'),
    path('staff/shipping'),    
    path('staff/shipping/add'),    
    path('staff/shipping/edit/<pk:pk>'),    
    path('staff/shipping/delete/<pk:pk>'),
    path('staff/report'),    
    path('staff/report/<pk:pk>'),    
]
