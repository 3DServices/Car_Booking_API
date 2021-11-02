import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDepartmentSerializer(ModelSerializer):
    organisation = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.Department
        fields = ['name', 'organisation']
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
        organisation = validated_data.pop('organisation', None)
        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        Department_instance = api_models.Department.objects.create(
            **validated_data, organisation=organisation_instances[0])
        return Department_instance


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = api_models.Department
        fields = ['id', 'name', 'organisation']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
