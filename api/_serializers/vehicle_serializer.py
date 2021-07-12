import api.models as api_models
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin


class VehicleSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Vehicle
        fields = '__all__'
        lookup_field = 'id'
        depth = 2

        extra_kwargs = {
            'id': {'validators': []},
        }
