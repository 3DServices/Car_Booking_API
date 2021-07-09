import api.models as api_models
import authentication.models as auth_models
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from api._serializers import project_vehicle_deploy_serializer as project_vehicle_deploy_serializer
from authentication.serializers import DriverSerializer


class VehicleSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Vehicle
        fields = '__all__'
        lookup_field = 'id'
        depth = 2

        extra_kwargs = {
            'id': {'validators': []},
        }


class OrganisationSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Organisation
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class OrganisationFleetManagerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.OrganisationFleetManager
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class OrganisationDriverSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.OrganisationDriver
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class OrganisationVehicleSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.OrganisationVehicle
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class ProjectSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Project
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class BranchSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Branch
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class StationSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Station
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class DepartmentSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Department
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class DirectorateSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Directorate
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class BlacklistSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Blacklist
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class PassengerBlacklistSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.PassengerBlacklist
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class DriverBlacklistSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.DriverBlacklist
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class VehicleBlacklistSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.VehicleBlacklist
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class TripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    vehicle = VehicleSerializer(required=True, write_only=True, many=True)
    driver = DriverSerializer(write_only=True, many=True)

    class Meta:
        model = api_models.Trip
        fields = ['id', 'vehicle', 'driver', 'pick_up_location',
                  'destination', 'date', 'time', 'reason', ]
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        vehicle_list = validated_data.pop('vehicle')
        driver_list = validated_data.pop('driver')
        vehicle_id = vehicle_list[0]['id']
        driver_id = driver_list[0]['id']
        vehicle = api_models.Vehicle.objects.get(id=vehicle_id)
        driver = auth_models.Driver.objects.get(id=driver_id)
        return api_models.Trip.objects.create(vehicle=vehicle, driver=driver, **validated_data)


class PassengerTripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.PassengerTrip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class FleetManagerTripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.FleetManagerTrip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class FleetManagerTripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.FleetManagerTrip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class DriverTripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.DriverTrip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


class StationVehicleDeploySerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.StationVehicleDeploy
        fields = '__all__'
        lookup_field = 'id'
        depth = 2
