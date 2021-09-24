import api._views.organisation_vehicle_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/',
         views.CreateOrganisationVehicleViewSet.as_view({'post': 'create'})),
    path('', views.ViewOrganisationVehiclesListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:id>/', views.RetrieveOrganisationVehicleViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateOrganisationVehicleViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteOrganisationVehicleViewSet.as_view({'delete': 'destroy'})),
]
