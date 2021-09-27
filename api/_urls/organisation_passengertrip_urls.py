import api._views.organisation_passengertrip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewOrganisationPassengerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateOrganisationPassengerTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveOrganisationPassengerTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateOrganisationPassengerTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteOrganisationPassengerTripViewSet.as_view({'delete': 'destroy'})),
]
