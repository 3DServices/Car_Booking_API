import api._views.organisation_fleet_manager_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateOrganisationFleetManagerViewSet.as_view({'post': 'create'})),
    path('', views.ViewOrganisationFleetManagersListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveOrganisationFleetManagerViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateOrganisationFleetManagerViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteOrganisationFleetManagerViewSet.as_view({'delete': 'destroy'})),
]
