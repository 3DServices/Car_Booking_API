import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreatePassengerBlacklistSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.PassengerBlacklist
        fields = ['reason', 'passenger']
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
        passenger = validated_data.pop('passenger', None)
        passenger_instances = auth_models.Passenger.objects.all().filter(id=passenger)

        if not passenger_instances.exists():
            raise ValidationError({'passenger': 'Invalid value!'})

        passenger_instance = passenger_instances[0]
        passenger_instance.is_available = False
        passenger_instance.save()

        blacklist_instance = api_models.Blacklist.objects.create(
            **validated_data)

        passenger_blacklist_instance = api_models.PassengerBlacklist.objects.create(
            passenger=passenger_instance, blacklist=blacklist_instance)

        return passenger_blacklist_instance


class PassengerBlacklistSerializer(ModelSerializer):
    class Meta:
        model = api_models.PassengerBlacklist
        fields = ['id', 'blacklist', 'passenger']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
