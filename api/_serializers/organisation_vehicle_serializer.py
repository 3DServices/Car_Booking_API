from rest_framework import fields
import api.models as api_models
from core.mixins.serializer_mixins import ModelSerializer
from api._serializers.vehicle_serializer import VehicleSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)


class CreateOrganisationVehicleSerializer(ModelSerializer):
    organisation = serializers.UUIDField()

    class Meta:
        model = api_models.Vehicle
        exclude = ["created_by", "lastupdated_by", "created_at",
                   "lastupdated_at", ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        organisation = validated_data.pop('organisation', None)

        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        vehicle_instance = api_models.Vehicle.objects.create(
            **validated_data
        )
        organisation_vehicle_instance = api_models.OrganisationVehicle.objects.create(
            vehicle=vehicle_instance,
            organisation=organisation_instances[0],
        )
        return organisation_vehicle_instance


class OrganisationVehicleSerializer(ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = api_models.OrganisationVehicle
        fields = ['id', 'vehicle']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
