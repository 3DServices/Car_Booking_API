from authentication.models import User, SystemAdmin, Driver, Passenger, FleetManager
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'id'


class SystemAdminSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = SystemAdmin
        fields = '__all__'
        depth = 1

class DriverSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = Driver
        fields = '__all__'
        depth = 1


class PassengerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = Passenger
        fields = '__all__'
        depth = 1


class FleetManagerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = FleetManager
        fields = '__all__'
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    # redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            print(token, uidb64)

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(Id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
