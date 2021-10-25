import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from api._serializers.department_serializers import DepartmentSerializer
from api._serializers.trip_serializer import TripSerializer
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDepartmentTripSerializer(ModelSerializer):
    department = serializers.UUIDField()
    pick_up_location = serializers.CharField(required=True, write_only=True)
    destination = serializers.CharField(required=True, write_only=True)
    date = serializers.DateTimeField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)
    vehicle = serializers.UUIDField(required=True, write_only=True)
    driver = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.DepartmentTrip
        fields = ['id', 'department', 'driver', 'pick_up_location',
                  'destination', 'date', 'reason', 'vehicle']
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
        department = validated_data.pop('department', None)
        vehicle = validated_data.pop('vehicle', None)
        driver = validated_data.pop('driver', None)

        vehicle_instances = api_models.Vehicle.objects.all().filter(id=vehicle)
        driver_instances = auth_models.Driver.objects.all().filter(id=driver)
        department_instances = api_models.Department.objects.all().filter(id=department)

        if not vehicle_instances.exists():
            raise ValidationError({'vehicle': 'Invalid value!'})

        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})

        if not department_instances.exists():
            raise ValidationError({'department': 'Invalid value!'})

        trip_instance = api_models.Trip.objects.create(
            driver=driver_instances[0],
            vehicle=vehicle_instances[0],
            **validated_data
        )
        department_trip_instance = api_models.DepartmentTrip.objects.create(
            department=department_instances[0],
            trip=trip_instance,
        )
        return department_trip_instance


class DepartmentTripSerializer(ModelSerializer):
    trip = TripSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = api_models.DepartmentTrip
        fields = ['id', 'trip', 'department']
        lookup_field = 'id'
        depth = 1

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
