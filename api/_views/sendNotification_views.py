
from rest_framework.response import Response
from business_logic.utilities.expo_notification import send_push_message
from rest_framework import status, generics
from api._serializers.send_notification_serializers import SendNotificationSerializer
from django.utils.timezone import utc
import datetime
from django.http import HttpResponse


class SendNotificationView(generics.GenericAPIView):
    serializer_class = SendNotificationSerializer

    def post(self, request, format=None):

        serializer = SendNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = request.data['token']
            response = send_push_message(token)
            results = response

            return Response(results, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
