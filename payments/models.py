from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def calculate_total_price(self):
        # Проверка, сохранен ли уже Order
        if self.pk:
            total = sum(item.price for item in self.items.all())
            discount_total = sum((d.discount_amount / 100) * total for d in self.discount_set.all())
            tax_total = sum((t.tax_amount / 100) * total for t in self.tax_set.all())
            return total - discount_total + tax_total
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