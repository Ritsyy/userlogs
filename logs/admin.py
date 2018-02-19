from django.contrib import admin
from .models import Item, Variant

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


class VariantAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(Variant, VariantAdmin)
