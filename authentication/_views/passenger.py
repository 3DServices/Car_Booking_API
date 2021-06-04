from django.shortcuts import render
from authentication.models import Passenger
from rest_framework import viewsets
from authentication.serializers import PassengerSerializer
from car_booking_api.mixins import view_mixins


# Create your views here.


class CreatePassengerViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewPassengersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

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


class RetrievePassengerViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdatePassengerViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeletePassengerViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
