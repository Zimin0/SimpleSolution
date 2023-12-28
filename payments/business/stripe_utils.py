import stripe
from payments.models import Order

class StripeSessionCreator:
    def __init__(self, order: Order):
        self.order = order
        stripe.api_key = 'sk_test_51OSFHsLoQoyi9wp2qWs9TDvwJRtxtgRHXQpakODubsbPU928OUrYzMqIWQMPXhkzCCpQKE2RP832R2ayqTgmmUKQ00sSMSkv4T'

    def create_session(self, success_url, cancel_url):
        line_items = self._generate_line_items()
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url
        )
        return session

    def _generate_line_items(self):
        line_items = []
        for item in self.order.items.all():
            # Применяем скидку и налог к каждому товару
            discount_total = sum((d.discount_amount / 100) * item.price for d in self.order.discount_set.all())
            tax_total = sum((t.tax_amount / 100) * item.price for t in self.order.tax_set.all())
            adjusted_price = item.price - discount_total + tax_total

            line_item = {
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(adjusted_price * 100),
                },
                'quantity': 1,
            }
            line_items.append(line_item)
        return line_items
