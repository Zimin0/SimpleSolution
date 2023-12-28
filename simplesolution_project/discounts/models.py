from django.db import models
from payments.models import Order
from django.core.validators import MinValueValidator, MaxValueValidator

class Discount(models.Model):
    """ Скидка в % """
    class Meta:
        verbose_name = "Скидка на заказ"
        verbose_name_plural = "Скидки на заказ"

    order = models.ForeignKey(
        Order, 
        verbose_name="Заказ", 
        related_name="discounts", 
        on_delete=models.CASCADE
        )
    discount_amount = models.DecimalField(
        verbose_name="Скидка(%)", 
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01), MaxValueValidator(100.00)]
    )

class Tax(models.Model):
    """ Налог в % """
    class Meta:
        verbose_name = "Налог на заказ"
        verbose_name_plural = "Налоги на заказ"

    order = models.ForeignKey(
        Order,
        verbose_name="Заказ",
        related_name="taxes",
        on_delete=models.CASCADE
        )
    
    tax_amount = models.DecimalField(
        verbose_name="Налог(%)",
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01), MaxValueValidator(100.00)]
    )