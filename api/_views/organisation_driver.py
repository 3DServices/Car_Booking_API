from django.shortcuts import render
from api.models import OrganisationDriver
from rest_framework import viewsets
from api.serializers import OrganisationDriverSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateOrganisationDriverViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationDriver.objects.all()
    serializer_class = OrganisationDriverSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewOrganisationDriversListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationDriver.objects.all()
    serializer_class = OrganisationDriverSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['driver']

    def get(self, request):
        if 'organisationdrivers' in cache:
            # get results from cache
            organisationdrivers = cache.get('organisationdrivers')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [organisationdriver.to_json()
                       for organisationdriver in queryset]
            # store data in cache
            cache.set('organisationdrivers', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveOrganisationDriverViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationDriver.objects.all()
    serializer_class = OrganisationDriverSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateOrganisationDriverViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationDriver.objects.all()
    serializer_class = OrganisationDriverSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteOrganisationDriverViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationDriver.objects.all()
    serializer_class = OrganisationDriverSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
