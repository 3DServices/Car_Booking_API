import api._views.organisation_trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewOrganisationTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateOrganisationTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveOrganisationTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateOrganisationTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteOrganisationTripViewSet.as_view({'delete': 'destroy'})),
]
