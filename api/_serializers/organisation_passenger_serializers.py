import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from api._serializers.organisation_serializers import OrganisationSerializer
from authentication._serializers.passenger_serializers import CreatePassengerSerializer, PassengerSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer
from business_logic.system_users._user import User as UserFacade


class CreateOrganisationPassengerSerializer(ModelSerializer):
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
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    organisation = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = api_models.OrganisationPassenger
        fields = ['email', 'password', 'organisation']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {'validators': []},
        }

    def create(self, validated_data):
        _request = self.context['request']
        organisation = validated_data.pop('organisation', None)

        organisation_instances = api_models.Organisation.objects.all().filter(id=organisation)

        if not organisation_instances.exists():
            raise ValidationError({'organisation': 'Invalid value!'})

        request = {'request': _request, 'validated_data': validated_data}
        passenger_registered = UserFacade().register_passenger(request)
        passenger_instances = auth_models.Passenger.objects.all()
        for passenger in passenger_instances:
            if(passenger.user.email == validated_data["email"]):
                organisation_passenger_instance = api_models.OrganisationPassenger.objects.create(
                    passenger=passenger, organisation=organisation_instances[0])

                return passenger_registered


class OrganisationPassengerSerializer(ModelSerializer):
    passenger = PassengerSerializer()

    class Meta:
        model = api_models.OrganisationPassenger
        fields = ['id', 'passenger']
        lookup_field = 'id'
        depth = 1

        extra_kwargs = {
            'id': {'validators': []},
        }
