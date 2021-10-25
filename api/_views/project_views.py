from django.shortcuts import render
from api.models import Project
from rest_framework import viewsets
from api.serializers import ProjectSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateProjectViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewProjectsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'projects' in cache:
            # get results from cache
            projects = cache.get('projects')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [project.to_json() for project in queryset]
            # store data in cache
            cache.set('projects', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveProjectViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateProjectViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteProjectViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
