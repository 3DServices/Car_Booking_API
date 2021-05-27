from django.shortcuts import render
from api.models import Organisation
from rest_framework import viewsets
from api.serializers import OrganisationSerializer
from car_booking_api.mixins import view_mixins


# Create your views here.


class CreateOrganisationViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewOrganisationsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'id'

    def get(self, request):
        try:
            return self.list(request)
        except Exception as exception:
            raise exception


class RetrieveOrganisationViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateOrganisationViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteOrganisationViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
