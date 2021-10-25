from django.shortcuts import render
from api.models import Department, DepartmentVehicle
from rest_framework import viewsets
from api._serializers.department_vehicle_serializer import CreateDepartmentVehicleSerializer, DepartmentVehicleSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters
from core.utilities.rest_exceptions import (ValidationError)

# Create your views here.


def _get_queryset(view_instance):
    try:
        department_id = view_instance.kwargs['department_id']

        _departments = Department.objects.filter(id=department_id)
        if not _departments.exists():
            raise ValidationError(
                {'department_id': 'department with the specified id does not exist!'})

        return DepartmentVehicle.objects.all().filter(department=_departments[0])
    except Exception as exception:
        raise exception


class CreateDepartmentVehicleViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentVehicle.objects.all()
    serializer_class = CreateDepartmentVehicleSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewDepartmentVehiclesListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentVehicle.objects.all()
    serializer_class = DepartmentVehicleSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['vehicle']

    def get(self, request):
        if 'departmentvehicles' in cache:
            # get results from cache
            departmentvehicles = cache.get('departmentvehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [departmentvehicle.to_json()
                       for departmentvehicle in queryset]
            # store data in cache
            cache.set('departmentvehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

    def get_queryset(self):
        return _get_queryset(self)


class RetrieveDepartmentVehicleViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentVehicle.objects.all()
    serializer_class = DepartmentVehicleSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class UpdateDepartmentVehicleViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentVehicle.objects.all()
    serializer_class = DepartmentVehicleSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class DeleteDepartmentVehicleViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentVehicle.objects.all()
    serializer_class = DepartmentVehicleSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)
