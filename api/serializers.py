import api.models as api_models

from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Vehicle
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Organisation
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class OrganisationFleetManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.OrganisationFleetManager
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class OrganisationDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.OrganisationDriver
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class OrganisationVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.OrganisationVehicle
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Project
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Branch
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Station
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Department
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class DirectorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Directorate
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Blacklist
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class PassengerBlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.PassengerBlacklist
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class DriverBlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.DriverBlacklist
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2


class VehicleBlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.VehicleBlacklist
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2
