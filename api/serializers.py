from api.models import Vehicle

from rest_framework import serializers


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','url', 'type_of_vehicle', 'brand']
        lookup_field = 'id'
        
