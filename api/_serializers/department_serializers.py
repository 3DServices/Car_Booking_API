import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDepartmentSerializer(ModelSerializer):

    class Meta:
        model = api_models.Department
        fields = ['name']
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

        Department_instance = api_models.Department.objects.create(
            **validated_data)
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
