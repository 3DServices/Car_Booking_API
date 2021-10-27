from api._serializers.organisation_driver_serializers import OrganisationDriverSerializer
import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDepartmentDriverSerializer(ModelSerializer):
    driver = serializers.UUIDField(required=True, write_only=True)
    department = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.DepartmentDriver
        fields = ['department', 'driver']
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
        department = validated_data.pop('department', None)
        driver_instances = api_models.OrganisationDriver.objects.all().filter(id=driver)
        department_instances = api_models.Department.objects.all().filter(id=department)

        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})
        if not department_instances.exists():
            raise ValidationError({'department': 'Invalid value!'})

        department_driver_instance = api_models.DepartmentDriver.objects.create(
            driver=driver_instances[0], department=department_instances[0])

        return department_driver_instance


class DepartmentDriverSerializer(ModelSerializer):
    driver = OrganisationDriverSerializer()

    class Meta:
        model = api_models.DepartmentDriver
        fields = ['id', 'driver']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
