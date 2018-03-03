from django.contrib.admin.models import LogEntry

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LogsSerializer, LogEntrySerializer
from .models import *


class WeavedinLogsView(APIView):
    allowed_methods = ['GET']
    serializer_class = LogsSerializer

    def get_object(self, request, user_id):
        try:
            return Item.objects.get(user=user_id)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, user_id=None):
        start_time = request.query_params.get('start_time', None)
        end_time = request.query_params.get('end_time', None)
        if start_time:
            log_entry = LogEntry.objects.filter(action_time__gte=start_time)
        if end_time:
            log_entry = LogEntry.objects.filter(action_time__lte=end_time)
        if user_id:
            items = Item.objects.filter(user=user_id)
        else:
            items = Item.objects.all()
        response = []
        for item in items:
            item_data = LogsSerializer(item).data
            logentires = log_entry.filter(object_id=item.id)
            log_data = LogEntrySerializer(logentires, many=True).data
            item_data['history'] = log_data
            variants = item.variant_set.all()
            for variant in variants:
                variantentries = log_entry.filter(object_id=variant.id)
                variant_data = LogEntrySerializer(variantentries, many=True).data
                item_data['variant_history'] = variant_data
            response.append(item_data)
        return Response(response)
