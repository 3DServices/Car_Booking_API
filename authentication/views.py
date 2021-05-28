from django.shortcuts import render
from authentication.models import User
from rest_framework import viewsets
from authentication.serializers import UserSerializer
import authentication._views.system_admin as system_admin_views
import authentication._views.driver as driver_views
import authentication._views.passenger as passenger_views
import authentication._views.fleet_manager as fleet_manager_views


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
