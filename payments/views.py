from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from payments.models import Item, Order
from payments.business.stripe_utils import StripeSessionCreator

def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)

    # Создаем новый заказ
    order = Order()
    order.save() 
    order.items.add(item)

    # Обновляем и сохраняем order после добавления item
    order.total_price = order.calculate_total_price()
    order.save()

    # Создание сессии Stripe
    stripe_creator = StripeSessionCreator(order)
    session = stripe_creator.create_session(
        success_url=request.build_absolute_uri(f'/success/?order_id={order.id}'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    return JsonResponse({'session_id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'payments/item_detail.html', {'item': item})
