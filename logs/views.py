from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LogsSerializer
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
        if user_id:
            item_id = user_id
            item = Item.objects.filter(user=item_id)
        else:
            item = Item.objects.all()
        serializer = LogsSerializer(item, many=True)

        response = Response(serializer.data)
        data = response.data
        result = []
        for i in data:
            value = dict(i)
            variant = Variant.objects.get(id=value['variant'])
            value['variant_history'] = variant.history.values()
            value['history'] = value['history'].values()
            for history in value['history']:
                if history['history_type'] == '+':
                    history['history_type'] = "Item Added"
                elif history['history_type'] == '~':
                    history['history_type'] = "Item Updated"
                elif history['history_type'] == '-':
                    history['history_type'] = "Item Deleted"
            for history in value['variant_history']:
                if history['history_type'] == '+':
                    history['history_type'] = "Variant Added"
                elif history['history_type'] == '~':
                    history['history_type'] = "Variant Updated"
                elif history['history_type'] == '-':
                    history['history_type'] = "Variant Deleted"
            result.append(value)

        result = Response(result)

        return result
