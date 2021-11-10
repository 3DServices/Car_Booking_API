import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer
from business_logic.system_users._user import User as UserFacade


class CreateOrganisationDriverSerializer(ModelSerializer):
    email = serializers.EmailField(
        max_length=254,
        min_length=5,
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        required=True,
        write_only=True,
        help_text='Required',
        style={'input_type': 'password', 'placeholder': 'Password'})

    organisation = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.OrganisationDriver
        fields = ['organisation', 'email', 'password']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}

        organisation = validated_data.pop('organisation', None)
        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        driver_registered = UserFacade().register_driver(request)
        driver_instances = auth_models.Driver.objects.all()
        for driver in driver_instances:
            if(driver.user.email == validated_data["email"]):
                organisation_driver_instance = api_models.OrganisationDriver.objects.create(
                    driver=driver, organisation=organisation_instances[0])

                return driver_registered


class OrganisationDriverSerializer(ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = api_models.OrganisationDriver
        fields = ['id', 'driver']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
