from django.shortcuts import get_object_or_404, render, redirect
from payments.models import Item, Order
from payments.business.stripe_utils import StripePaymentIntentCreator
from django.views.decorators.http import require_POST, require_GET

@require_POST
def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)
    order = Order()
    order.save() 
    order.items.add(item)

    return redirect('payments:pay_order', order_id=order.id)

@require_GET
def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'payments/item_detail.html', {'item': item})

@require_GET
def pay_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    stripe_creator = StripePaymentIntentCreator(order)
    payment_intent = stripe_creator.create_payment_intent()

    return render(request, 'payments/payment_form.html', {
        'client_secret': payment_intent.client_secret,
        'order': order
    })

def payment_success(request):
    return render(request, 'payments/success.html')