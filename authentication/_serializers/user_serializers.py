from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from allauth.account.models import EmailAddress
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from authentication.models import User
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

        EmailAddress.objects.create(
            user=user, email=user.email, verified=True, primary=True)
        return user

class UserSerializer(ModelSerializer):
    # address = useraddress_serializers()
    class Meta:
        model = User
        exclude = [
            'password', 
            'is_superuser', 
            'username', 
            'is_staff',
            'is_active', 
            'groups', 
            'user_permissions'
            ]
        extra_kwargs={
            'is_verified': {'write_only':True},
            'is_admin': {'write_only':True},
                'is_medihub_staff': {'write_only':True},
                'is_vendor': {'write_only':True},
                'is_courier': {'write_only':True},
                'is_client': {'write_only':True},
            }
        depth = 3
