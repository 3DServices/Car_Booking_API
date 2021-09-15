from rest_framework import serializers
from business_logic.utilities.expo_notification import send_push_message
from authentication.models import *
from api.models import *
from core.utilities.rest_exceptions import (ValidationError)


class SendNotification:
    def __init__(self, token):
        self.token = token


class SendNotificationSerializer(serializers.Serializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    trip = serializers.UUIDField(required=True, write_only=True)

    def create(self, validated_data):
        passenger = validated_data.pop('passenger')

        passenger_instances = Passenger.objects.all().filter(id=passenger)
        if not passenger_instances.exists():
            raise ValidationError({'passenger': 'Passenger doesnt exist !'})

        passenger_notification_instances = PassengerNotification.objects.filter(
            passenger=passenger_instances[0])

        if not passenger_notification_instances.exists():
            raise ValidationError(
                {'passenger': 'Passenger has not yet regisered his application to receive notifications !'})

        token = passenger_notification_instances[0].notification.expo_token

        # send_push_message(token)

        return token
