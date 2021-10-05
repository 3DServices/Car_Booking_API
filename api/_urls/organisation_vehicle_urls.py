import api._views.organisation_vehicle_views as views
from django.urls import path


urlpatterns = [
    path(r'create/',
         views.CreateOrganisationVehicleViewSet.as_view({'post': 'create'})),
    path('<str:organisation_id>/', views.ViewOrganisationVehiclesListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'<str:organisation_id>/<str:id>/', views.RetrieveOrganisationVehicleViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:organisation_id>/<str:id>/update/',
         views.UpdateOrganisationVehicleViewSet.as_view({'put': 'update'})),
    path(r'<str:organisation_id>/<str:id>/delete/',
         views.DeleteOrganisationVehicleViewSet.as_view({'delete': 'destroy'})),
]
