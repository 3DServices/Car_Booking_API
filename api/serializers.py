import api.models as api_models
import authentication.models as auth_models
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from api._serializers import project_vehicle_deploy_serializer as project_vehicle_deploy_serializer
from authentication.serializers import DriverSerializer
from api._serializers.trip_serializer import (
    TripSerializer, CreateTripSerializer)
from api._serializers.vehicle_serializer import VehicleSerializer


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


class DirectorateSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Directorate
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
