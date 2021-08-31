from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from authentication.models import Profile
from core.mixins.serializer_mixins import ModelSerializer


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'username',
                  'first_name', 'last_name', 'gender']
        exclude = []
        extra_kwargs = {
            'id': {'read_only': True},
        }
        depth = 0
