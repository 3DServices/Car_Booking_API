import api._views.fleet_manager_trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewFleetManagerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateFleetManagerTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveFleetManagerTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateFleetManagerTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteFleetManagerTripViewSet.as_view({'delete': 'destroy'})),
]
