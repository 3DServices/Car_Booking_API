from api.models import DepartmentDriver, DepartmentFleetManager, DriverRating, Organisation, OrganisationDriver, OrganisationFleetManager, DepartmentPassenger, OrganisationPassenger, PassengerRating
from api._serializers.organisation_serializers import OrganisationSerializer
from api._serializers.userphonenumber_serializers import UserPhoneNumberSerializer
from django.db.models import fields
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
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
    rating = serializers.SerializerMethodField()

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
        organisation = {
            "organisation_id": None,
            "organisation_name": None,
            "department_id": None,
            "department_name": None
        }

        _user = User.objects.get(Id=obj.Id)

        if _user.is_passenger:

            _passenger = Passenger.objects.filter(user=_user.Id)

            if _passenger.exists():
                _organisationpassenger = OrganisationPassenger.objects.all().filter(
                    passenger=_passenger[0])

                if _organisationpassenger.exists():
                    organisationpassenger = _organisationpassenger[0]
                    organisation["organisation_id"] = organisationpassenger.organisation.id
                    organisation["organisation_name"] = organisationpassenger.organisation.name

                    _departmentpassenger = DepartmentPassenger.objects.all().filter(
                        passenger=_organisationpassenger[0])

                    if _departmentpassenger.exists():
                        departmentpassenger = _departmentpassenger[0]
                        organisation["department_id"] = departmentpassenger.department.id
                        organisation["department_name"] = departmentpassenger.department.name

                return organisation

        if _user.is_driver:

            _driver = Driver.objects.filter(user=_user.Id)
            if _driver.exists():

                _organisationdriver = OrganisationDriver.objects.all().filter(
                    driver=_driver[0])

                if _organisationdriver.exists():
                    organisationdriver = _organisationdriver[0]

                    organisation["organisation_id"] = organisationdriver.organisation.id
                    organisation["organisation_name"] = organisationdriver.organisation.name

                    _departmentdriver = DepartmentDriver.objects.all().filter(
                        driver=_organisationdriver[0])

                    if _departmentdriver.exists():
                        departmentdriver = _departmentdriver[0]
                        organisation["department_id"] = departmentdriver.department.id
                        organisation["department_name"] = departmentdriver.department.name
                return organisation

        if _user.is_fleetmanager:

            _fleetmanager = FleetManager.objects.filter(user=_user.Id)
            if _fleetmanager.exists():

                _organisationfleetmanager = OrganisationFleetManager.objects.all().filter(
                    fleet_manager=_fleetmanager[0])

                if _organisationfleetmanager.exists():
                    organisationfleetmanager = _organisationfleetmanager[0]
                    organisation["organisation_id"] = organisationfleetmanager.organisation.id
                    organisation["organisation_name"] = organisationfleetmanager.organisation.name

                    _departmentfleetmanager = DepartmentFleetManager.objects.all().filter(
                        fleet_manager=_organisationfleetmanager[0])

                    if _departmentfleetmanager.exists():
                        departmentfleetmanager = _departmentfleetmanager[0]
                        organisation["department_id"] = departmentfleetmanager.department.id
                        organisation["department_name"] = departmentfleetmanager.department.name
                return organisation

        return org

    def get_rating(self, obj):

        _user = User.objects.get(Id=obj.Id)

        if _user.is_passenger:

            _passenger = Passenger.objects.filter(user=_user.Id)

            if _passenger.exists():
                _passenger_rating = PassengerRating.objects.all().filter(
                    passenger=_passenger[0])

                if _passenger_rating.exists():
                    ratings = []
                    for rating in _passenger_rating:
                        ratings.append(rating.rating.rate_value)
                    return sum(ratings) / len(ratings)

        if _user.is_driver:

            _driver = Driver.objects.filter(user=_user.Id)

            if _driver.exists():
                _driver_rating = DriverRating.objects.all().filter(
                    driver=_driver[0])

                if _driver_rating.exists():
                    ratings = []
                    for rating in _driver_rating:
                        ratings.append(rating.rating.rate_value)
                    return int(sum(ratings) / len(ratings))

        return 0
