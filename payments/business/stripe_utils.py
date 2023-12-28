import stripe
from payments.models import Order

class StripeSessionCreator:
    def __init__(self, order: Order):
        self.order = order
        stripe.api_key = 'sk_test_51OSFHsLoQoyi9wp2qWs9TDvwJRtxtgRHXQpakODubsbPU928OUrYzMqIWQMPXhkzCCpQKE2RP832R2ayqTgmmUKQ00sSMSkv4T'

    def create_session(self, success_url, cancel_url):
            line_items = self._generate_line_items()
            # Используем валюту первого товара в заказе
            currency = self.order.items.first().currency

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
                currency=currency,  # Добавляем валюту
            )
            return session

    def _generate_line_items(self):
        line_items = []
        for item in self.order.items.all():
            # Используем related_name для доступа к скидкам и налогам
            discount_total = sum((discount.discount_amount / 100) * item.price for discount in self.order.discounts.all())
            tax_total = sum((tax.tax_amount / 100) * item.price for tax in self.order.taxes.all())
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
