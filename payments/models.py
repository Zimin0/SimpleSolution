from django.db import models

class Item(models.Model):
    CURRENCY = (
        ("RUB", "Рубли"),
        ("EUR", "Евро"),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY)

class Order(models.Model):
    items = models.ManyToManyField(Item)

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

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super(Order, self).save(*args, **kwargs)

class Discount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)  # процент скидки

class Tax(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)  # процент налога