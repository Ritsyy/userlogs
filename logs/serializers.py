from rest_framework import serializers

from .models import Item


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('history', 'user', 'name', 'brand', 'category', 'product_code', 'variant')
