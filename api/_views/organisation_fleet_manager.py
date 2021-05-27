from django.shortcuts import render
from api.models import OrganisationFleetManager
from rest_framework import viewsets
from api.serializers import OrganisationFleetManagerSerializer
from car_booking_api.mixins import view_mixins


# Create your views here.


class CreateOrganisationFleetManagerViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationFleetManager.objects.all()
    serializer_class = OrganisationFleetManagerSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewOrganisationFleetManagersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationFleetManager.objects.all()
    serializer_class = OrganisationFleetManagerSerializer
    lookup_field = 'id'

    def get(self, request):
        try:
            return self.list(request)
        except Exception as exception:
            raise exception


class RetrieveOrganisationFleetManagerViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationFleetManager.objects.all()
    serializer_class = OrganisationFleetManagerSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateOrganisationFleetManagerViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationFleetManager.objects.all()
    serializer_class = OrganisationFleetManagerSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteOrganisationFleetManagerViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrganisationFleetManager.objects.all()
    serializer_class = OrganisationFleetManagerSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
