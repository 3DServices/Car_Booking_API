from api.models import Organisation, OrganisationDriver, OrganisationFleetManager, OrganisationPassenger
from api._serializers.organisation_serializers import OrganisationSerializer
from api._serializers.userphonenumber_serializers import UserPhoneNumberSerializer
from django.db.models import fields
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from authentication.models import Driver, FleetManager, Passenger, User
from api._serializers.phonenumber_serializers import PhoneNumberSerializer

from core.mixins.serializer_mixins import ModelSerializer


class RegisterUserSerializer(ModelSerializer):
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)

        # EmailAddress.objects.create(
        #     user=user, email=user.email, verified=True, primary=True)
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
            'is_fleetmanager',
            'is_systemadmin',
            'is_driver',
            'is_passenger',
            'is_verified',
            "last_login"
        ]
        extra_kwargs = {
            'is_verified': {'write_only': True},
            'is_admin': {'write_only': True},
            'is_passenger': {'write_only': True},
            'is_driver': {'write_only': True},
            'is_systemadmin': {'write_only': True},
            'is_fleetmanager': {'write_only': True},
        }
        depth = 3


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
            'is_fleetmanager',
            'is_systemadmin',
            'is_driver',
            'is_passenger',
            'is_verified',
            "last_login"
        ]
        extra_kwargs = {
            'is_verified': {'write_only': True},
            'is_admin': {'write_only': True},
            'is_passenger': {'write_only': True},
            'is_driver': {'write_only': True},
            'is_systemadmin': {'write_only': True},
            'is_fleetmanager': {'write_only': True},
        }
        depth = 3


class UserProfileSerializer(ModelSerializer):
    phone_number = PhoneNumberSerializer(read_only=True, many=True)
    organisation = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'username',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'is_verified',
            "last_login"

        ]

        depth = 3

    def get_organisation(self, obj):
        org = None

        _user = User.objects.get(Id=obj.Id)

        if _user.is_passenger:

            _passenger = Passenger.objects.get(user=_user.Id)
            _organisationpassenger = OrganisationPassenger.objects.all().filter(passenger=_passenger)
            organisationpassenger = _organisationpassenger[0]
            return organisationpassenger.organisation.name

        if _user.is_driver:

            _driver = Driver.objects.get(user=_user.Id)
            _organisationdriver = OrganisationDriver.objects.all().filter(driver=_driver)
            organisationdriver = _organisationdriver[0]
            return organisationdriver.organisation.name

        if _user.is_fleetmanager:

            _fleetmanager = FleetManager.objects.get(user=_user.Id)
            _organisationfleetmanager = OrganisationFleetManager.objects.all().filter(
                fleet_manager=_fleetmanager)
            organisationfleetmanager = _organisationfleetmanager[0]
            return organisationfleetmanager.organisation.name

        return org
