from django.shortcuts import render
from authentication.models import FleetManager
from rest_framework import viewsets
from authentication.serializers import FleetManagerSerializer
from car_booking_api.mixins import view_mixins


# Create your views here.


class CreateFleetManagerViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FleetManager.objects.all()
    serializer_class = FleetManagerSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewFleetManagersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FleetManager.objects.all()
    serializer_class = FleetManagerSerializer
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


class RetrieveFleetManagerViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FleetManager.objects.all()
    serializer_class = FleetManagerSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateFleetManagerViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FleetManager.objects.all()
    serializer_class = FleetManagerSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteFleetManagerViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FleetManager.objects.all()
    serializer_class = FleetManagerSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
