from django.shortcuts import render
from authentication.models import User
from rest_framework import viewsets
from authentication.serializers import UserSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
