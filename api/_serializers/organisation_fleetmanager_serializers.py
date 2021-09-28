import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer
from authentication._serializers.fleet_manager_serializers import FleetManagerSerializer


class CreateOrganisationFleetManagerSerializer(ModelSerializer):
    fleet_manager = serializers.UUIDField(required=True, write_only=True)
    organisation = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.OrganisationFleetManager
        fields = ['organisation', 'fleet_manager']
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
        fleet_manager = validated_data.pop('fleet_manager', None)
        organisation = validated_data.pop('organisation', None)
        fleet_manager_instances = auth_models.FleetManager.objects.all().filter(id=fleet_manager)
        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not fleet_manager_instances.exists():
            raise ValidationError({'fleet_manager': 'Invalid value!'})
        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        organisation_fleet_manager_instance = api_models.OrganisationFleetManager.objects.create(
            fleet_manager=fleet_manager_instances[0], organisation=organisation_instances[0])

        return organisation_fleet_manager_instance


class OrganisationFleetManagerSerializer(ModelSerializer):
    fleet_manager = FleetManagerSerializer()

    class Meta:
        model = api_models.OrganisationFleetManager
        fields = ['id', 'organisation', 'fleet_manager']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
