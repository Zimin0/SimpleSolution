from django.db import models

class Item(models.Model):
    """ Товар в магазине """
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    CURRENCY = (
        ("RUB", "Рубли"),
        ("EUR", "Евро"),
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

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super(Order, self).save(*args, **kwargs)

    def calculate_total_price(self):
        if self.pk:
            total = 0
            for item in self.items.all():
                item_price = item.price
                discount_total = sum((d.discount_amount / 100) * item_price for d in self.discounts.all())
                tax_total = sum((t.tax_amount / 100) * item_price for t in self.taxes.all())
                total += item_price - discount_total + tax_total
            return total
        else:
            return 0
