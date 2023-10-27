from django.contrib import admin
from pos.hotdog_stands.models import HotDogStand, InventoryItem, Inventory, Sale, SaleItem, Discount

class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1
    fields = ['item', 'quantity', 'threshold']

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1
    fields = ['inventory_item', 'quantity', 'price']

class HotDogStandAdmin(admin.ModelAdmin):
    list_display = ['id', 'operator', 'location']
    inlines = [InventoryInline]

class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotdog_stand', 'time']
    inlines = [SaleItemInline]

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percentage']

admin.site.register(HotDogStand, HotDogStandAdmin)
admin.site.register(InventoryItem)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Discount, DiscountAdmin)
