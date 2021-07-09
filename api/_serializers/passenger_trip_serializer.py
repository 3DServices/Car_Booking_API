import api.models as api_models
import authentication.models as auth_models
from rest_framework import serializers, status
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from authentication.serializers import DriverSerializer, PassengerSerializer
from api.serializers import TripSerializer
from authentication._serializers.passenger_serializers import PassengerSerializer


class CreatePassengerTripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):

    trip = TripSerializer(required=True)
    passenger = PassengerSerializer(required=True)
    data = serializers.DictField(
        required=False,
        read_only=True,
    )

    class Meta:
        model = api_models.PassengerTrip
        fields = ['id', 'trip', 'passenger', 'data']

        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        trip_list = validated_data.pop('trip')
        trip_id = trip_list['id']
        trip = api_models.Trip.objects.get(id=trip_id)

        passenger_list = validated_data.pop('passenger')
        passenger_id = passenger_list['id']
        passenger = auth_models.Passenger.objects.get(id=passenger_id)

        return api_models.PassengerTrip.objects.create(trip=trip, passenger=passenger)


class PassengerTripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.PassengerTrip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2
