import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDriverBlacklistSerializer(ModelSerializer):
    driver = serializers.UUIDField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.DriverBlacklist
        fields = ['reason', 'driver']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        driver = validated_data.pop('driver', None)
        driver_instances = auth_models.Driver.objects.all().filter(id=driver)

        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})

        blacklist_instance = api_models.Blacklist.objects.create(
            **validated_data)

        driver_blacklist_instance = api_models.DriverBlacklist.objects.create(
            driver=driver_instances[0], blacklist=blacklist_instance)

        return driver_blacklist_instance


class DriverBlacklistSerializer(ModelSerializer):
    class Meta:
        model = api_models.DriverBlacklist
        fields = ['id', 'blacklist', 'driver']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {'validators': []},
        }
