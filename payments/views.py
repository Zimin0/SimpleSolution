from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Item
import stripe

stripe.api_key = 'pk_test_51OSFHsLoQoyi9wp2qmJ5Pip54W8HNcDLBWcj4DEp824ZIt0zoF33axcrvVlP7o2kdbexbQzEfCGnn1TFY27mf8or00akYSyoV3'

def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'session_id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item_detail.html', {'item': item})
