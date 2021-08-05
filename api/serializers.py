import api.models as api_models
import authentication.models as auth_models
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from api._serializers import project_vehicle_deploy_serializer as project_vehicle_deploy_serializer
from authentication.serializers import DriverSerializer
from api._serializers.trip_serializer import (
    TripSerializer, CreateTripSerializer)
from api._serializers.vehicle_serializer import VehicleSerializer


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
