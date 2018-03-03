from django.contrib import admin
from .models import Item, Variant
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


class VariantAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(Variant, VariantAdmin)
