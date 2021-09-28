import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateOrganisationDriverSerializer(ModelSerializer):
    driver = serializers.UUIDField(required=True, write_only=True)
    organisation = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.OrganisationDriver
        fields = ['organisation', 'driver']
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
        driver = validated_data.pop('driver', None)
        organisation = validated_data.pop('organisation', None)
        driver_instances = auth_models.Driver.objects.all().filter(id=driver)
        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})
        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        organisation_driver_instance = api_models.OrganisationDriver.objects.create(
            driver=driver_instances[0], organisation=organisation_instances[0])

        return organisation_driver_instance


class OrganisationDriverSerializer(ModelSerializer):
    class Meta:
        model = api_models.OrganisationDriver
        fields = ['id', 'organisation', 'driver']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
