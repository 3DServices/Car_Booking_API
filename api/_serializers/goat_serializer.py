import api.models as api_models
import authentication.models as auth_models
from authentication.serializers import DriverSerializer, PassengerSerializer
from api.serializers import TripSerializer
from authentication._serializers.passenger_serializers import PassengerSerializer
from core.mixins.serializer_mixins import ModelSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from django.utils import timezone


class CreateGoatSerializer(ModelSerializer):
    user = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.Goat
        fields = ['id', 'name', 'description', 'breed', 'user']
        lookup_field = 'id'
        depth = 1

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        user = validated_data.pop('user', None)

        user_instances = auth_models.Passenger.objects.all().filter(id=user)

        if not user_instances.exists():
            raise ValidationError({'user': 'Invalid value!'})

        goat_instance = api_models.Goat.objects.create(
            user=user_instances[0],
            **validated_data
        )
        return goat_instance


class GoatSerializer(ModelSerializer):

    class Meta:
        model = api_models.Goat
        fields = ['id', 'name', 'description', 'breed', 'user']
        lookup_field = 'id'
        depth = 1
