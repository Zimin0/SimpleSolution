import stripe
from payments.models import Order
import requests
from decimal import Decimal

class StripePaymentIntentCreator:
    def __init__(self, order: Order):
        self.order = order
        stripe.api_key = 'sk_test_51OSFHsLoQoyi9wp2qWs9TDvwJRtxtgRHXQpakODubsbPU928OUrYzMqIWQMPXhkzCCpQKE2RP832R2ayqTgmmUKQ00sSMSkv4T'

    def create_payment_intent(self):
        # Расчет общей суммы заказа и валюты
        amount, currency = self._calculate_order_total()

        # Создание намерения платежа в Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card'],
        )
        return payment_intent

    def _get_usd_conversion_rate(self, currency):
        if currency == 'usd':
            return 1.0  # Конвертация не требуется, если валюта - USD

        # Получение курса конвертации в USD
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{currency}')
        data = response.json()
        return data['rates']['USD']

    def _calculate_adjusted_price(self, item):
        # Расчет скорректированной цены товара с учетом скидок и налогов
        discount_total = sum((d.discount_amount / 100) * item.price for d in self.order.discounts.all())
        tax_total = sum((t.tax_amount / 100) * item.price for t in self.order.taxes.all())
        return item.price - discount_total + tax_total

    def _calculate_order_total(self):
        items = list(self.order.items.all())
        if len(items) == 1:
            # Если в заказе только один товар, используем его валюту и цену напрямую
            item = items[0]
            adjusted_price = self._calculate_adjusted_price(item)
            return int(adjusted_price * 100), item.currency
        else:
            # Если товары в разных валютах, конвертируем все в USD
            total_in_usd = Decimal(0)
            for item in items:
                conversion_rate = Decimal(self._get_usd_conversion_rate(item.currency))
                adjusted_price = self._calculate_adjusted_price(item)
                total_in_usd += adjusted_price * conversion_rate
            return int(total_in_usd * 100), 'usd'
