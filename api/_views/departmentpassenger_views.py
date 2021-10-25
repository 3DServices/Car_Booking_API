from django.shortcuts import render
from api.models import Department, DepartmentPassenger
from rest_framework import viewsets
from api._serializers.department_passenger_serializers import DepartmentPassengerSerializer, CreateDepartmentPassengerSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters
from core.utilities.rest_exceptions import (ValidationError)

# Create your views here.


def _get_queryset(view_instance):
    try:
        department_id = view_instance.kwargs['department_id']

        # 03. Validate Vendor

        # ...
        _departments = Department.objects.filter(
            id=department_id)
        if not _departments.exists():
            raise ValidationError(
                {'department_id': 'department with the specified id does not exist!'})

        return DepartmentPassenger.objects.all().filter(department=_departments[0])
    except Exception as exception:
        raise exception


class CreateDepartmentPassengerViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentPassenger.objects.all()
    serializer_class = CreateDepartmentPassengerSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewAllDepartmentPassengersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentPassenger.objects.all()
    serializer_class = DepartmentPassengerSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'departments' in cache:
            # get results from cache
            departments = cache.get('departments')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [department.to_json() for department in queryset]
            # store data in cache
            cache.set('departments', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class ViewDepartmentPassengersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentPassenger.objects.all()
    serializer_class = DepartmentPassengerSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'departments' in cache:
            # get results from cache
            departments = cache.get('departments')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [department.to_json() for department in queryset]
            # store data in cache
            cache.set('departments', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

    def get_queryset(self):
        return _get_queryset(self)


class RetrieveDepartmentPassengerViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentPassenger.objects.all()
    serializer_class = DepartmentPassengerSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class UpdateDepartmentPassengerViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentPassenger.objects.all()
    serializer_class = DepartmentPassengerSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class DeleteDepartmentPassengerViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DepartmentPassenger.objects.all()
    serializer_class = DepartmentPassengerSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)
