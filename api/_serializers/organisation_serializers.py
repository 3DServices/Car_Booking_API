import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateOrganisationSerializer(ModelSerializer):

    class Meta:
        model = api_models.Organisation
        fields = ['name']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}

        Organisation_instance = api_models.Organisation.objects.create(
            **validated_data)
        return Organisation_instance


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = api_models.Organisation
        fields = ['id', 'name', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {'validators': []},
        }
