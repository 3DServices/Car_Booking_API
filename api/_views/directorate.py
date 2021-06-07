from django.shortcuts import render
from api.models import Directorate
from rest_framework import viewsets
from api.serializers import DirectorateSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateDirectorateViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Directorate.objects.all()
    serializer_class = DirectorateSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewDirectoratesListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Directorate.objects.all()
    serializer_class = DirectorateSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'directorates' in cache:
            # get results from cache
            directorates = cache.get('directorates')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [directorate.to_json() for directorate in queryset]
            # store data in cache
            cache.set('directorates', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveDirectorateViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Directorate.objects.all()
    serializer_class = DirectorateSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateDirectorateViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Directorate.objects.all()
    serializer_class = DirectorateSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteDirectorateViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Directorate.objects.all()
    serializer_class = DirectorateSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
