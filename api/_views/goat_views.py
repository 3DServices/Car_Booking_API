from django.shortcuts import render
from api.models import Goat
from authentication.models import Passenger
from rest_framework import viewsets
from api._serializers.goat_serializer import GoatSerializer, CreateGoatSerializer
from car_booking_api.mixins import view_mixins
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from car_booking_api import filters
from core.utilities.rest_exceptions import (ValidationError)


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.


def _get_queryset(view_instance):
    try:
        user_id = view_instance.kwargs['user_id']

        # 03. Validate Vendor

        # ...
        _passengers = Passenger.objects.filter(id=user_id)
        if not _passengers.exists():
            raise ValidationError(
                {'user_id': 'passenger with the specified id does not exist!'})

        return Goat.objects.all().filter(user=_passengers[0])
    except Exception as exception:
        raise exception


class CreateGoatViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goat.objects.all()
    serializer_class = CreateGoatSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewGoatsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['type_of_vehicle', 'brand']

    def get(self, request):
        if 'vehicles' in cache:
            # get results from cache
            vehicles = cache.get('vehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('vehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

    def get_queryset(self):
        return _get_queryset(self)


class ViewAllGoatsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['type_of_vehicle', 'brand']

    def get(self, request):
        if 'vehicles' in cache:
            # get results from cache
            vehicles = cache.get('vehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('vehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveGoatViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class UpdateGoatViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class DeleteGoatViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)
