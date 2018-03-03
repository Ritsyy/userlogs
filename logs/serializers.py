from rest_framework import serializers
from django.contrib.admin.models import LogEntry
from .models import Item


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('user', 'name', 'brand', 'category', 'product_code',)


class LogEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = LogEntry
        fields = ('change_message', 'user', 'action_time' )
