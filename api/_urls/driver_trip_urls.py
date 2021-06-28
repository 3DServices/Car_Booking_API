import api._views.driver_trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewDriverTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateDriverTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveDriverTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateDriverTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDriverTripViewSet.as_view({'delete': 'destroy'})),
]
