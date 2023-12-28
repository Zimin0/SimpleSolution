import stripe
from payments.models import Order

class StripePaymentIntentCreator:
    def __init__(self, order: Order):
        self.order = order
        stripe.api_key = 'sk_test_51OSFHsLoQoyi9wp2qWs9TDvwJRtxtgRHXQpakODubsbPU928OUrYzMqIWQMPXhkzCCpQKE2RP832R2ayqTgmmUKQ00sSMSkv4T'

    def create_payment_intent(self):
        amount = self._calculate_order_total()
        currency = self.order.items.first().currency

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card'],
        )
        return payment_intent

    def _calculate_order_total(self):
        total = 0
        for item in self.order.items.all():
            discount_total = sum((d.discount_amount / 100) * item.price for d in self.order.discounts.all())
            tax_total = sum((t.tax_amount / 100) * item.price for t in self.order.taxes.all())
            adjusted_price = item.price - discount_total + tax_total
            total += adjusted_price
        return int(total * 100)  # Возвращаем сумму в центах
