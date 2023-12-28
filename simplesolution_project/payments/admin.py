from django.contrib import admin
from payments.models import Item, Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'currency']
    search_fields = ['name', 'currency'] 
    list_filter = ['currency'] 
    ordering = ['name']  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_items', 'calculate_total_price']
    
    def get_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    get_items.short_description = 'Items'

    search_fields = ['id']  
    ordering = ['id']  