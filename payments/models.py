from django.db import models

class Item(models.Model):
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
    class Meta:
        verbose_name = "Заказ на покупку"
        verbose_name_plural = "Заказы на покупку"

    items = models.ManyToManyField(Item, verbose_name="Товары в заказе")
    
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
                discount_total = sum((d.discount_amount / 100) * item_price for d in self.discount_set.all())
                tax_total = sum((t.tax_amount / 100) * item_price for t in self.tax_set.all())
                total += item_price - discount_total + tax_total
            return total
        else:
            return 0


class Discount(models.Model):
    class Meta:
        verbose_name = "Скидка на заказ"
        verbose_name_plural = "Скидки на заказ"
    
    def __str__(self):
        return f"{self.id}"

    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.CASCADE)
    discount_amount = models.DecimalField(verbose_name="Скидка(%)", max_digits=5, decimal_places=2) 

class Tax(models.Model):
    class Meta:
        verbose_name = "Налог на заказ"
        verbose_name_plural = "Налоги на заказ"
    
    def __str__(self):
        return f"{self.id}"

    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.CASCADE)
    tax_amount = models.DecimalField(verbose_name="Скидка(%)", max_digits=10, decimal_places=2)