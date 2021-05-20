from api.models import Vehicle

from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        lookup_field = 'id'
        # depth = 2
        
