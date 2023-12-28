from django.contrib import admin
from discounts.models import Discount, Tax

@admin.register(Discount)
class Discount(admin.ModelAdmin):
    list_display = ['order', 'discount_amount']

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['order', 'tax_amount']