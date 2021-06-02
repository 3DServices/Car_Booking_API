from authentication.models import User, SystemAdmin, Driver, Passenger, FleetManager
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin


class UserSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'id'


class SystemAdminSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = SystemAdmin
        fields = '__all__'
        depth = 1

class DriverSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = Driver
        fields = '__all__'
        depth = 1


class PassengerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = Passenger
        fields = '__all__'
        depth = 1


class FleetManagerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = FleetManager
        fields = '__all__'
        depth = 1
