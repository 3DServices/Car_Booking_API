import api.models as api_models
import authentication.models as auth_models
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from authentication.serializers import DriverSerializer, PassengerSerializer
from api.serializers import TripSerializer
from authentication._serializers.passenger_serializers import PassengerSerializer
from core.mixins.serializer_mixins import ModelSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)


class CreatePassengerTripSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    pick_up_location = serializers.CharField(required=True, write_only=True)
    destination = serializers.CharField(required=True, write_only=True)
    date = serializers.DateField(required=True, write_only=True)
    time = serializers.TimeField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)
    vehicle = serializers.UUIDField(required=True, write_only=True)
    driver = serializers.UUIDField(required=True, write_only=True)

    data = serializers.DictField(
        required=False,
        read_only=True,
    )

    class Meta:
        model = api_models.PassengerTrip
        fields = ['id', 'vehicle', 'driver', 'pick_up_location',
                  'destination', 'date', 'time', 'reason', 'passenger', 'data']

        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        try:
            _request = self.context['request']
            request = {'request': _request, 'validated_data': validated_data}
            vehicle = validated_data.pop('vehicle', None)
            driver = validated_data.pop('driver', None)
            passenger = validated_data.pop('passenger', None)

            if not passenger:
                raise ValidationError({'passenger': 'This field is required!'})

            if not vehicle:
                raise ValidationError({'vehicle': 'This field is required!'})

            if not driver:
                raise ValidationError({'driver': 'This field is required!'})

            vehicle_instances = api_models.Vehicle.objects.all().filter(id=vehicle)
            driver_instances = auth_models.Driver.objects.all().filter(id=driver)
            passenger_instances = auth_models.Passenger.objects.all().filter(id=passenger)

            if not vehicle_instances.exists():
                raise ValidationError({'vehicle': 'Invalid value!'})

            if not driver_instances.exists():
                raise ValidationError({'driver': 'Invalid value!'})

            if not passenger_instances.exists():
                raise ValidationError({'passenger': 'Invalid value!'})

            trip_instance = api_models.Trip.objects.create(
                driver=driver_instances[0],
                vehicle=vehicle_instances[0],
                **validated_data
            )

            passenger_trip_instance = api_models.PassengerTrip.objects.create(
                passenger=passenger_instances[0],
                trip=trip_instance,
                # **validated_data
            )

            return passenger_trip_instance

        except Exception as exception:
            raise exception

        # return api_models.PassengerTrip.objects.create(trip=trip, passenger=passenger)


class PassengerTripSerializer(ModelSerializer):
    class Meta:
        model = api_models.PassengerTrip
        fields = ['id', 'trip', 'passenger']
        lookup_field = 'id'
        depth = 1
