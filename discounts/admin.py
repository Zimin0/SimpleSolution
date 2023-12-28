from django.contrib import admin
from discounts.models import Discount, Tax

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['order', 'discount_amount']
    search_fields = ['order__id']  
    list_filter = ['order']  
    ordering = ['order'] 

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['order', 'tax_amount']
    search_fields = ['order__id']  
    list_filter = ['order']  
    ordering = ['order']  