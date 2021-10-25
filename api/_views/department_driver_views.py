from django.shortcuts import render
from api.models import Department, DepartmentDriver
from rest_framework import viewsets
from api._serializers.department_driver_serializers import DepartmentDriverSerializer, CreateDepartmentDriverSerializer
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

        return DepartmentDriver.objects.all().filter(department=_departments[0])
    except Exception as exception:
        raise exception


class CreateDepartmentDriverViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentDriver.objects.all()
    serializer_class = CreateDepartmentDriverSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewDepartmentDriversListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentDriver.objects.all()
    serializer_class = DepartmentDriverSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['driver']

    def get(self, request):
        if 'departmentdrivers' in cache:
            # get results from cache
            departmentdrivers = cache.get('departmentdrivers')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [departmentdriver.to_json()
                       for departmentdriver in queryset]
            # store data in cache
            cache.set('departmentdrivers', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

    def get_queryset(self):
        return _get_queryset(self)


class RetrieveDepartmentDriverViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentDriver.objects.all()
    serializer_class = DepartmentDriverSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class UpdateDepartmentDriverViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentDriver.objects.all()
    serializer_class = DepartmentDriverSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class DeleteDepartmentDriverViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentDriver.objects.all()
    serializer_class = DepartmentDriverSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)
