from rest_framework import fields
import api.models as api_models
from core.mixins.serializer_mixins import ModelSerializer
from api._serializers.vehicle_serializer import VehicleSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)


class CreateDepartmentVehicleSerializer(ModelSerializer):
    department = serializers.UUIDField()

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
        department = validated_data.pop('department', None)

        department_instances = api_models.Department.objects.all().filter(id=department)

        if not department_instances.exists():
            raise ValidationError({'department': 'Invalid value!'})

        vehicle_instance = api_models.Vehicle.objects.create(
            **validated_data
        )
        department_vehicle_instance = api_models.DepartmentVehicle.objects.create(
            vehicle=vehicle_instance,
            department=department_instances[0],
        )
        return department_vehicle_instance


class DepartmentVehicleSerializer(ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = api_models.DepartmentVehicle
        fields = ['id', 'vehicle']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
