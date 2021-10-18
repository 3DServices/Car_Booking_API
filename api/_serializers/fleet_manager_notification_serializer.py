import api.models as api_models
import authentication.models as auth_models
from authentication._serializers.fleet_manager_serializers import FleetManagerSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateFleetManagerNotificationSerializer(ModelSerializer):
    fleet_manager = serializers.UUIDField(required=True, write_only=True)
    expo_token = serializers.CharField(
        required=True, write_only=True, max_length=255)

    class Meta:
        model = api_models.FleetManagerNotification
        fields = ['expo_token', 'fleet_manager']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        expo_token = validated_data.pop('expo_token', None)
        fleet_manager = validated_data.pop('fleet_manager', None)

        if not fleet_manager:
            raise ValidationError({'fleet_manager': 'This field is required!'})
        if not expo_token:
            raise ValidationError({'expo_token': 'This field is required!'})

        fleet_manager_instances = auth_models.FleetManager.objects.all().filter(id=fleet_manager)
        notification_instances = api_models.Notification.objects.all().filter(
            expo_token=expo_token)

        if not fleet_manager_instances.exists():
            raise ValidationError({'fleet_manager': 'Invalid value!'})

        if not notification_instances.exists():
            notification_instance = api_models.Notification.objects.create(
                expo_token=expo_token)
        else:
            notification_instance = notification_instances[0]

        fleet_manager_notification_instance = api_models.FleetManagerNotification.objects.create(fleet_manager=fleet_manager_instances[0], notification=notification_instance
                                                                                                 )
        return fleet_manager_notification_instance


class FleetManagerNotificationSerializer(ModelSerializer):
    class Meta:
        model = api_models.FleetManagerNotification
        fields = ['id', 'fleet_manager', 'notification', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
