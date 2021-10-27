from api._serializers.organisation_passenger_serializers import OrganisationPassengerSerializer
import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from api._serializers.department_serializers import DepartmentSerializer
from authentication._serializers.passenger_serializers import PassengerSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDepartmentPassengerSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    department = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.DepartmentPassenger
        fields = ['department', 'passenger']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        passenger = validated_data.pop('passenger', None)
        department = validated_data.pop('department', None)
        passenger_instances = api_models.OrganisationPassenger.objects.all().filter(id=passenger)
        department_instances = api_models.Department.objects.all().filter(id=department)

        if not passenger_instances.exists():
            raise ValidationError(
                {'passenger': 'Passenger Doesnt exist in the organisation!'})
        if not department_instances.exists():
            raise ValidationError({'department': 'Invalid value!'})

        department_passenger_instance = api_models.DepartmentPassenger.objects.create(
            passenger=passenger_instances[0], department=department_instances[0])

        return department_passenger_instance


class DepartmentPassengerSerializer(ModelSerializer):
    passenger = OrganisationPassengerSerializer()

    class Meta:
        model = api_models.DepartmentPassenger
        fields = ['id', 'passenger']
        lookup_field = 'id'
        depth = 1

        extra_kwargs = {
            'id': {'validators': []},
        }
