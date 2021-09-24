import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateOrganisationPassengerSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    organisation = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.OrganisationPassenger
        fields = ['organisation', 'passenger']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        passenger = validated_data.pop('passenger', None)
        organisation = validated_data.pop('organisation', None)
        passenger_instances = auth_models.Passenger.objects.all().filter(id=passenger)
        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not passenger_instances.exists():
            raise ValidationError({'passenger': 'Invalid value!'})
        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        organisation_passenger_instance = api_models.OrganisationPassenger.objects.create(
            passenger=passenger_instances[0], organisation=organisation_instances[0])

        return organisation_passenger_instance


class OrganisationPassengerSerializer(ModelSerializer):
    class Meta:
        model = api_models.OrganisationPassenger
        fields = ['id', 'organisation', 'passenger']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {'validators': []},
        }
