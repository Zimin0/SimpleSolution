from django.db import models

class Item(models.Model):
    """ Товар в магазине """
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    CURRENCY = (
        ("RUB", "Рубль"),
        ("USD", "Доллар"),
    )

    name = models.CharField(verbose_name="Название", max_length=200)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    currency = models.CharField(verbose_name="Валюта", max_length=3, choices=CURRENCY)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    """ Заказ. Содержит в себе Items """
    class Meta:
        verbose_name = "Заказ на покупку"
        verbose_name_plural = "Заказы на покупку"

    items = models.ManyToManyField(Item, related_name="orders", verbose_name="Товары в заказе")
    
    def __str__(self):
        return f"{self.id}"

    def display_prices(self):
        result = {}
        for item in self.items.all():
            currency = item.currency
            if currency not in result:
                result[currency] = 0

            discount_total = sum((d.discount_amount / 100) * item.price for d in self.discounts.all())
            tax_total = sum((t.tax_amount / 100) * item.price for t in self.taxes.all())
            adjusted_price = item.price - discount_total + tax_total
            result[currency] += adjusted_price

        # Формируем строку с результатами
        total_strings = [f"{currency}: {int(amount)}" for currency, amount in result.items()]
        return ' '.join(total_strings)
