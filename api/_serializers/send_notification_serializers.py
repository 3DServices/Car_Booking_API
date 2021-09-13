from rest_framework import serializers
from business_logic.utilities.expo_notification import send_push_message


class SendNotification:
    def __init__(self, token):
        self.token = token


class SendNotificationSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        token = validated_data.pop('token')
        return SendNotification(token)
