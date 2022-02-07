import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from api._serializers.vehicle_serializer import VehicleSerializer
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateEquipmentBookingSerializer(ModelSerializer):
    driver = serializers.UUIDField(required=True, write_only=True)
    equipment = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.EquipmentBooking
        fields = ['id', 'driver','equipment', 'pick_up_location',
                  'destination', 'date', 'reason']
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
        equipment = validated_data.pop('equipment', None)

        
        if not driver:
            raise ValidationError({'driver': 'This field is required!'})

        if not equipment:
            raise ValidationError({'equipment': 'This field is required!'})

        driver_instances = auth_models.Driver.objects.all().filter(id=driver)
        equipment_instances = api_models.Equipment.objects.all().filter(id=equipment)

        
        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})

        if not equipment_instances.exists():
            raise ValidationError({'equipment': 'Invalid value!'})

        

        equipment_booking_instance = api_models.EquipmentBooking.objects.create(
            driver=driver_instances[0],
            equipment=equipment_instances[0],
            **validated_data
        )
        return equipment_booking_instance


class EquipmentBookingSerializer(ModelSerializer):
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = api_models.EquipmentBooking
        fields = ['id',  'driver', 'pick_up_location',
                  'destination', 'date', 'reason', 'status']
        lookup_field = 'id'
        depth = 1

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
