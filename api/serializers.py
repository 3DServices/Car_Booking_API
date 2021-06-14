import api.models as api_models

from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin


class VehicleSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Vehicle
        fields = '__all__'
        lookup_field = 'id'
        depth = 2


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
    class Meta:
        model = api_models.Trip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2

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