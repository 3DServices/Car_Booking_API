import api.models as api_models

from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin


class TripSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = api_models.Trip
        fields = '__all__'
        lookup_field = 'id'
        depth = 2
