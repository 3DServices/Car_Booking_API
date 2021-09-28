from django.shortcuts import render
from api.models import OrganisationVehicle
from rest_framework import viewsets
from api._serializers.organisation_vehicle_serializer import CreateOrganisationVehicleSerializer, OrganisationVehicleSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateOrganisationVehicleViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationVehicle.objects.all()
    serializer_class = CreateOrganisationVehicleSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewOrganisationVehiclesListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationVehicle.objects.all()
    serializer_class = OrganisationVehicleSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['vehicle']

    def get(self, request):
        if 'organisationvehicles' in cache:
            # get results from cache
            organisationvehicles = cache.get('organisationvehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [organisationvehicle.to_json()
                       for organisationvehicle in queryset]
            # store data in cache
            cache.set('organisationvehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveOrganisationVehicleViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationVehicle.objects.all()
    serializer_class = OrganisationVehicleSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateOrganisationVehicleViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationVehicle.objects.all()
    serializer_class = OrganisationVehicleSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteOrganisationVehicleViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationVehicle.objects.all()
    serializer_class = OrganisationVehicleSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
