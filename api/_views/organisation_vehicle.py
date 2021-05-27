from django.shortcuts import render
from api.models import OrganisationVehicle
from rest_framework import viewsets
from api.serializers import OrganisationVehicleSerializer
from car_booking_api.mixins import view_mixins


# Create your views here.


class CreateOrganisationVehicleViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationVehicle.objects.all()
    serializer_class = OrganisationVehicleSerializer
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

    def get(self, request):
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
