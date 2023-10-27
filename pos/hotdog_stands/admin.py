from django.contrib import admin

from pos.hotdog_stands.models import Discount, HotDogStand, Inventory, InventoryItem, Sale, SaleItem


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1
    fields = ["item", "quantity", "threshold"]


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1
    fields = ["inventory_item", "quantity", "price"]


@admin.register(HotDogStand)
class HotDogStandAdmin(admin.ModelAdmin):
    list_display = ["id", "operator", "location"]
    inlines = [InventoryInline]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["id", "hotdog_stand", "time"]
    inlines = [SaleItemInline]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "percentage"]


admin.site.register(InventoryItem)
