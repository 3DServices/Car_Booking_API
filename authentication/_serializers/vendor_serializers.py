from rest_framework import serializers

from authentication.models import User, Vendor
from business_logic.system_users._user import User as UserFacade
from core.mixins.serializer_mixins import ModelSerializer
from business_logic.utilities.mailing import EmailVerificationLinkSender


class CreateVendorSerializer(ModelSerializer):
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
    data = serializers.DictField(
        required=False,
        read_only=True,
        )

    class Meta:
        model = User
        fields = ['email', 'password','data']

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request':_request, 'validated_data':validated_data}
        return UserFacade().register_vendor(request)


class VendorSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.filter(is_superuser = False))
    class Meta:
        model = Vendor
        fields = '__all__'
        depth = 2
