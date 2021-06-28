import api._views.passenger_trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewPassengerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreatePassengerTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrievePassengerTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdatePassengerTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeletePassengerTripViewSet.as_view({'delete': 'destroy'})),
]
