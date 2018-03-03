from rest_framework import serializers
from django.contrib.admin.models import LogEntry
from .models import Item, Variant


class LogsSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField()

    def get_variants(self, obj):
        variant = obj.variant_set.all()
        variant_serializer = VariantSerializer(variant, many=True)
        return variant_serializer.data

    class Meta:
        model = Item
        fields = ('user', 'name', 'brand', 'category', 'product_code', 'variants')


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variant
        fields = '__all__'


class LogEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = LogEntry
        fields = ('change_message', 'user', 'action_time' )
