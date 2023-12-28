from django.contrib import admin

from payments.models import Item, Order, Discount, Tax

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'currency']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_items', 'calculate_total_price']
    def get_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    get_items.short_description = 'Items'

@admin.register(Discount)
class Discount(admin.ModelAdmin):
    list_display = ['order', 'discount_amount']

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['order', 'tax_amount']