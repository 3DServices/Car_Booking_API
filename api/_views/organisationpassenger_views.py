from django.shortcuts import render
from api.models import OrganisationPassenger
from rest_framework import viewsets
from api._serializers.organisation_passenger_serializers import OrganisationPassengerSerializer, CreateOrganisationPassengerSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters
from core.utilities.rest_exceptions import (ValidationError)

# Create your views here.


def _get_queryset(view_instance):
    try:
        organisation_id = view_instance.kwargs['organisation_id']

        # 03. Validate Vendor

        # ...
        _organisations = OrganisationPassenger.objects.filter(
            id=organisation_id)
        if not _organisations.exists():
            raise ValidationError(
                {'organisation_id': 'organisation with the specified id does not exist!'})

        return OrganisationPassenger.objects.all().filter(organisation=_organisations[0])
    except Exception as exception:
        raise exception


class CreateOrganisationPassengerViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationPassenger.objects.all()
    serializer_class = CreateOrganisationPassengerSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewAllOrganisationPassengersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationPassenger.objects.all()
    serializer_class = OrganisationPassengerSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'organisations' in cache:
            # get results from cache
            organisations = cache.get('organisations')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [organisation.to_json() for organisation in queryset]
            # store data in cache
            cache.set('organisations', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class ViewOrganisationPassengersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationPassenger.objects.all()
    serializer_class = OrganisationPassengerSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'organisations' in cache:
            # get results from cache
            organisations = cache.get('organisations')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [organisation.to_json() for organisation in queryset]
            # store data in cache
            cache.set('organisations', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

    def get_queryset(self):
        return _get_queryset(self)


class RetrieveOrganisationPassengerViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationPassenger.objects.all()
    serializer_class = OrganisationPassengerSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class UpdateOrganisationPassengerViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationPassenger.objects.all()
    serializer_class = OrganisationPassengerSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class DeleteOrganisationPassengerViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationPassenger.objects.all()
    serializer_class = OrganisationPassengerSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)
