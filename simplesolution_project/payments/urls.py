from django.urls import path
from payments.views import buy_item, item_detail, pay_order, payment_success

app_name = 'payments'

urlpatterns = [
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('item/<int:id>/', item_detail, name='item_detail'),
    path('pay-order/<int:order_id>/', pay_order, name='pay_order'),
    path('success/', payment_success, name='payment_success'),
]