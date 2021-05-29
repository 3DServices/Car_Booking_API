from authentication.models import User, SystemAdmin, Driver, Passenger, FleetManager
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'id'


class SystemAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SystemAdmin
        fields = '__all__'


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class FleetManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FleetManager
        fields = '__all__'
