from django.shortcuts import render
from api.models import PassengerBlacklist
from rest_framework import viewsets
from api._serializers.passenger_blacklist_serializers import PassengerBlacklistSerializer, CreatePassengerBlacklistSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreatePassengerBlacklistViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerBlacklist.objects.all()
    serializer_class = CreatePassengerBlacklistSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewPassengerBlacklistsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerBlacklist.objects.all()
    serializer_class = PassengerBlacklistSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['passenger']

    def get(self, request):
        if 'passengerblacklists' in cache:
            # get results from cache
            passengerblacklists = cache.get('passengerblacklists')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [passengerblacklist.to_json()
                       for passengerblacklist in queryset]
            # store data in cache
            cache.set('passengerblacklists', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrievePassengerBlacklistViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerBlacklist.objects.all()
    serializer_class = PassengerBlacklistSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdatePassengerBlacklistViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerBlacklist.objects.all()
    serializer_class = PassengerBlacklistSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeletePassengerBlacklistViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerBlacklist.objects.all()
    serializer_class = PassengerBlacklistSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
