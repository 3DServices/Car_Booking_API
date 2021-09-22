import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreatePassengerRatingSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    rate_value = serializers.FloatField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.PassengerRating
        fields = ['rate_value', 'reason', 'passenger']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        passenger = validated_data.pop('passenger', None)

        if not passenger:
            raise ValidationError({'passenger': 'This field is required!'})

        passenger_instances = auth_models.Passenger.objects.all().filter(id=passenger)

        if not passenger_instances.exists():
            raise ValidationError({'passenger': 'Invalid value!'})

        rate_instance = api_models.Rating.objects.create(**validated_data)

        passenger_rating_instance = api_models.PassengerRating.objects.create(
            rating=rate_instance, passenger=passenger_instances[0])
        return passenger_rating_instance


class PassengerRatingSerializer(ModelSerializer):
    class Meta:
        model = api_models.PassengerRating
        fields = ['id', 'rating', 'passenger', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {'validators': []},
        }
